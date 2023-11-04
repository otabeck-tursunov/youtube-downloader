const authorIcon = document.querySelector('.fa-chevron-left');
const muallif = document.querySelector('.muallif');

const author = document.querySelector('.author');

const infoIcon = document.querySelector('.infoIcon');
const info = document.querySelector('.info');

authorIcon,muallif.addEventListener('click', () =>{
    author.classList.toggle('authorHide')
    authorIcon.style.transform = "rotate(-90deg)";

    if(author.classList.contains('authorHide')){
        authorIcon.style.transform = "rotate(90deg)";
    }
});

infoIcon.addEventListener('click', () =>{
    info.classList.toggle('infoHide');

    infoIcon.style.color = "#03C988";
    infoIcon.style.transform = "rotate(-45deg)";
    if(info.classList.contains('infoHide')){
        infoIcon.style.color = "#fff";
        infoIcon.style.transform = "rotate(0deg)";
    }
})