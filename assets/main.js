(function () {
  const root = document.documentElement;
  const saved = localStorage.getItem("theme");
  if (saved === "light" || saved === "dark") {
    root.setAttribute("data-theme", saved);
  }

  const toggle = document.getElementById("theme-toggle");
  function syncLabel() {
    if (!toggle) return;
    const isLight = root.getAttribute("data-theme") === "light";
    toggle.textContent = isLight ? "Dark mode" : "Light mode";
  }
  syncLabel();

  if (toggle) {
    toggle.addEventListener("click", () => {
      const next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      syncLabel();
    });
  }

  document.querySelectorAll("pre").forEach((pre) => {
    const wrap = document.createElement("div");
    wrap.className = "code-wrap";
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);

    const btn = document.createElement("button");
    btn.className = "copy-btn";
    btn.type = "button";
    btn.textContent = "Copy";
    btn.addEventListener("click", async () => {
      const text = pre.innerText.trim();
      try {
        await navigator.clipboard.writeText(text);
        btn.textContent = "Copied!";
        setTimeout(() => {
          btn.textContent = "Copy";
        }, 1600);
      } catch {
        btn.textContent = "Failed";
      }
    });
    wrap.appendChild(btn);
  });
})();
