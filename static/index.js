window.addEventListener("scroll",function(){
    var headerr=document.querySelector('nav');
    headerr.classList.toggle("sticky",window.scrollY>0);
})

var cotroller=new ScrollMagic.Controller();
var scene=new ScrollMagic.Scene({
    triggerElement:'.fadescroll'
})
.setClassToggle('.fadescroll','show')
.addTo(controller);