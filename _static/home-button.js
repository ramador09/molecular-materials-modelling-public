// Inject a "Home" link (-> ramador.me, the umbrella portfolio) into the
// sphinx-book-theme top-right article toolbar, beside the repository / launch /
// theme-toggle buttons. Uses the theme's own button markup so it matches exactly.
(function () {
  function addHomeButton() {
    var bar = document.querySelector(".article-header-buttons");
    if (!bar || bar.querySelector(".home-portfolio-link")) return;
    var a = document.createElement("a");
    a.href = "https://ramador.me/";
    a.className = "btn btn-sm home-portfolio-link";
    a.title = "Home — ramador.me";
    a.setAttribute("aria-label", "Home — ramador.me");
    a.setAttribute("data-bs-placement", "bottom");
    a.setAttribute("data-bs-toggle", "tooltip");
    a.innerHTML = '<span class="btn__icon-container"><i class="fa-solid fa-house"></i></span>';
    bar.insertBefore(a, bar.firstChild);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addHomeButton);
  } else {
    addHomeButton();
  }
})();
