(function () {
  var editor = document.getElementById('play-editor');
  var consoleEl = document.getElementById('play-console');
  var runBtn = document.getElementById('play-run');
  var clearBtn = document.getElementById('play-clear');
  var sampleBtn = document.getElementById('play-sample');

  if (!editor || !consoleEl || !runBtn || !clearBtn || !sampleBtn) {
    return;
  }

  var samples = [
    {
      key: 'sample_hello',
      code: 'print("Hola OPN");\nvar a = 5;\nvar b = 7;\nprint(a + b);'
    },
    {
      key: 'sample_loop',
      code: 'var total = 0;\nfor (var i = 1; i <= 5; i = i + 1) {\n  total = total + i;\n}\nprint(total);'
    },
    {
      key: 'sample_func',
      code: 'function suma(a, b) {\n  return a + b;\n}\nprint(suma(8, 12));'
    }
  ];

  var sampleIndex = 0;

  function appendLine(text, isError) {
    var line = document.createElement('div');
    line.textContent = text;
    if (isError) {
      line.className = 'console-line-error';
    }
    consoleEl.appendChild(line);
  }

  function clearConsole() {
    consoleEl.textContent = '';
  }

  function transpileOPN(source) {
    var js = source.replace(/\bfunc\b/g, 'function');
    js = js.replace(/\bprint\s*\(/g, '__print(');
    js = js.replace(/\bimport\s*\(/g, '__import(');
    return js;
  }

  function runCode() {
    clearConsole();
    var code = editor.value || '';

    try {
      var transpiled = transpileOPN(code);
      var fn = new Function('__print', '__import', '"use strict";\n' + transpiled);
      fn(function (value) {
        appendLine(String(value));
      }, function (name) {
        appendLine('import() no esta soportado en el playground: ' + name, true);
        return null;
      });
    } catch (error) {
      appendLine(error.name + ': ' + error.message, true);
    }
  }

  function loadSample() {
    sampleIndex = (sampleIndex + 1) % samples.length;
    editor.value = samples[sampleIndex].code;
  }

  runBtn.addEventListener('click', runCode);
  clearBtn.addEventListener('click', clearConsole);
  sampleBtn.addEventListener('click', loadSample);

  editor.value = samples[0].code;
})();
