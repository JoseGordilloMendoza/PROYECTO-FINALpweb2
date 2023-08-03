document.addEventListener("DOMContentLoaded", function () {
  const dropdownMenus = document.querySelectorAll(".categories__item");

  dropdownMenus.forEach((menu) => {
    menu.addEventListener("click", function () {
      const dropdown = this.querySelector(".header__menu__dropdown");
      dropdown.style.display = dropdown.style.display === "none" ? "block" : "none";
    });
  });
});
