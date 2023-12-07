window.addEventListener("DOMContentLoaded", (event) => {
  var navbarShrink = function () {
    const navbarCollapsible = document.body.querySelector("#mainNav");
    if (!navbarCollapsible) {
      return;
    }
    if (window.scrollY === 0) {
      navbarCollapsible.classList.remove("navbar-shrink");
    } else {
      navbarCollapsible.classList.add("navbar-shrink");
    }
  };

  navbarShrink();

  document.addEventListener("scroll", navbarShrink);

  const mainNav = document.body.querySelector("#mainNav");
  if (mainNav) {
    new bootstrap.ScrollSpy(document.body, {
      target: "#mainNav",
      rootMargin: "0px 0px -40%",
    });
  }
});

document.addEventListener("DOMContentLoaded", function(){
  if (window.innerWidth < 992) {
  
    document.querySelectorAll('.navbar .dropdown').forEach(function(everydropdown){
      everydropdown.addEventListener('hidden.bs.dropdown', function () {
          this.querySelectorAll('.submenu').forEach(function(everysubmenu){
            everysubmenu.style.display = 'none';
          });
      })
    })
}});