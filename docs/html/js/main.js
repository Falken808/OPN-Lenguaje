(function () {
  var menuBtn = document.querySelector('[data-menu-toggle]');
  var nav = document.querySelector('[data-main-nav]');

  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      nav.classList.toggle('is-open');
      var expanded = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', String(!expanded));
    });
  }

  var currentPath = window.location.pathname.replace(/\\/g, '/');
  var links = document.querySelectorAll('[data-main-nav] a');
  links.forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href || href.indexOf('http') === 0 || href.indexOf('#') === 0) {
      return;
    }

    var normalized = href.replace(/\\/g, '/');
    if (currentPath.endsWith(normalized)) {
      link.classList.add('active');
    }
  });

  var i18n = window.OPN_I18N || {};
  var langButtons = document.querySelectorAll('[data-lang-switch]');

  function setLanguage(lang) {
    var chosen = i18n[lang] ? lang : 'en';
    localStorage.setItem('opn-lang', chosen);
    document.documentElement.lang = chosen;

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var key = el.getAttribute('data-i18n');
      var value = i18n[chosen] && i18n[chosen][key];
      if (typeof value === 'string') {
        if (el.hasAttribute('data-i18n-html')) {
          el.innerHTML = value;
        } else {
          el.textContent = value;
        }
      }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
      var key = el.getAttribute('data-i18n-placeholder');
      var value = i18n[chosen] && i18n[chosen][key];
      if (typeof value === 'string') {
        el.setAttribute('placeholder', value);
      }
    });

    langButtons.forEach(function (button) {
      button.classList.toggle('is-active', button.getAttribute('data-lang-switch') === chosen);
    });

    document.dispatchEvent(new CustomEvent('opn:langchange', { detail: { lang: chosen } }));
  }

  langButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      setLanguage(button.getAttribute('data-lang-switch'));
    });
  });

  var savedLang = localStorage.getItem('opn-lang') || document.documentElement.lang || 'en';
  setLanguage(savedLang);

  document.querySelectorAll('[data-copy-target]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var target = document.querySelector(btn.getAttribute('data-copy-target'));
      if (!target) {
        return;
      }

      var old = btn.textContent;
      var lang = document.documentElement.lang || 'es';
      var copiedText = (i18n[lang] && i18n[lang].copied) || 'Copiado';
      var errorText = (i18n[lang] && i18n[lang].copy_error) || 'Error';

      navigator.clipboard.writeText(target.innerText).then(function () {
        btn.textContent = copiedText;
        setTimeout(function () {
          btn.textContent = old;
        }, 1200);
      }).catch(function () {
        btn.textContent = errorText;
      });
    });
  });
})();
