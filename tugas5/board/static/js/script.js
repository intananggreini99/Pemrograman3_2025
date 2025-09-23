// toogle class active

// mencari elemen navbar outside
const navbarPlus = document.querySelector(".navbar-plus input");
const navbarOutside = document.querySelector(".navbar-outside ul");
// Ketika sidebar menu diklik akan menjalankan
// menacari elemen ber id menu (#menu)

navbarPlus.addEventListener("click", function () {
  navbarOutside.classList.toggle("slide");
});
