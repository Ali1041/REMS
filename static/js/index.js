    b=document.getElementsByName('body')
    x=document.getElementById('btn');
    y=document.getElementById('side-menu');
    p=document.getElementById('btn-1');
    console.log(window.innerWidth)
    if (window.innerWidth>1000){
        p.style.display='none'
        console.log('here')
    }
    else{
        p.style.display='block'
        console.log('wwdc')
    }
    x.addEventListener('click',()=>{
        y.classList.remove('fade-in');
        y.classList.add('fade-out')
    })
    p.addEventListener('click',()=>{
        y.classList.remove('fade-out');
        y.classList.add('fade-in')
    })
    l=document.getElementsByClassName('alert');
    setTimeout(()=>{

    },3000)