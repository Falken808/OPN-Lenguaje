(function () {
  var revealNodes = document.querySelectorAll('.reveal');
  if (revealNodes.length) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });

    revealNodes.forEach(function (node) {
      observer.observe(node);
    });
  }

  var tabContainers = document.querySelectorAll('[data-command-tabs]');
  tabContainers.forEach(function (container) {
    var tabs = container.querySelectorAll('.command-tab');
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        var targetId = tab.getAttribute('data-tab-target');
        var wrapper = tab.closest('[data-command-group]');
        if (!wrapper || !targetId) {
          return;
        }

        wrapper.querySelectorAll('.command-tab').forEach(function (item) {
          item.classList.remove('is-active');
        });

        wrapper.querySelectorAll('.command-panel').forEach(function (panel) {
          panel.classList.remove('is-active');
        });

        tab.classList.add('is-active');
        var panel = wrapper.querySelector('#' + targetId);
        if (panel) {
          panel.classList.add('is-active');
        }
      });
    });
  });

  document.querySelectorAll('.progress-fill[data-progress]').forEach(function (bar) {
    var target = Number(bar.getAttribute('data-progress')) || 0;
    requestAnimationFrame(function () {
      bar.style.width = Math.max(0, Math.min(100, target)) + '%';
    });
  });
})();
