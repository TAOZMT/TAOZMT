(function(){
    "use strict";
    const header=document.getElementById('header');
    if (header) {
        const headerScrolled = () => {
          if (window.scrollY > 150) {
            if(header.classList.contains('header-scrolled')===false){
              header.classList.add('header-scrolled');
            }
            
          } else {
              header.classList.remove('header-scrolled');           
          }
        }
        window.addEventListener('load', headerScrolled);
        document.addEventListener('scroll',headerScrolled);
    }
    const openNav=document.querySelector("#open-nav");
    const closeNav=document.querySelector("#close-nav");
    openNav.addEventListener("click",()=>{
        document.querySelector(".mobile-nav").classList.add("show");
    });
    closeNav.addEventListener("click",()=>{
        document.querySelector(".mobile-nav").classList.remove("show");
    });
    /**
   * Back to top button
   */
    const backtotop =document.getElementById('back-to-top');
    if (backtotop) {
    const toggleBacktotop = () => {
        if (window.scrollY > 100) {
        backtotop.classList.add('open')
        } else {
        backtotop.classList.remove('open')
        }
    }
    window.addEventListener('load', toggleBacktotop)
    document.addEventListener('scroll',toggleBacktotop);
    }
 })();