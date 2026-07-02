// Privacy-friendly, cookie-free page-view counting (GoatCounter), matching the
// portfolio site (ramador.goatcounter.com). It loads ONLY on the public site
// (ramador.me) — never on the gated *.pages.dev solutions twin — so author
// visits to the solutions never pollute the public stats. GoatCounter counts by
// path, so each course shows up separately in the one dashboard.
(function () {
  if (location.hostname !== "ramador.me") return;
  var s = document.createElement("script");
  s.async = true;
  s.src = "//gc.zgo.at/count.js";
  s.setAttribute("data-goatcounter", "https://ramador.goatcounter.com/count");
  document.head.appendChild(s);
})();
