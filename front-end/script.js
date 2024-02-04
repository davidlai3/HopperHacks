function toggleLogin() {
    document.querySelector(".overlay").classList.toggle("open");
  }

  const forms = document.querySelector(".forms"),
      links = document.querySelectorAll(".link");
    
links.forEach(link => {
    link.addEventListener("click", e => {
       e.preventDefault(); //preventing form submit
       forms.classList.toggle("show-signup");
    })
})