console.log("Welcome to Suggestion page"); 

//audioElemet.play()
// let songIndex = 0;
// var audioSrc = previewUrl;
// let audioElement = new Audio('audioSrc');
// let masterPlay = document.getElementById('masterPlay');
// let myProgressBar = document.getElementById('myProgressBar');

// let songs = [
//     {songName: "song", filePath: "templates\song.mp3"}
// ]

masterPlay.addEventListener('click', ()=>{
    if (audioElement.paused || audioElement.currentTime<=0){
        audioElement.play();
        masterPlay.classList.remove('fa-play');
        masterPlay.classList.add('fa-pause');
    }
    else {
        audioElement.pause();
        masterPlay.classList.remove('fa-pause');
        masterPlay.classList.add('fa-play');
    }
})
audioElement.addEventListener('timeupdate', ()=>{
    

    progress = parseInt((audioElement.currentTime/audioElement.duration)*100);
    
    myProgressBar.value = progress;
})

myProgressBar.addEventListener('change',()=>{
    audioElement.currentTime = myProgressBar.value * audioElement.duration/100;
})

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
    console.log(entry)
    if(entry.isIntersecting){
        entry.target.classList.add('show');
    }  
    else{
        entry.target.classList.remove('show');
    }      
    });
})

const hidddenElements = document.querySelectorAll('.hidden');
hidddenElements.forEach((el) => observer.observe(el));

const currentTime = document.querySelector('.current-time');
const musicDuration = document.querySelector('.song-duration');

currentTime.innerHTML = '00:00';

setTimeout(()=> {
    musicDuration.innerHTML = formatTime(audioElement.duration);
    myProgressBar.max = audioElement.duration;
    setInterval(() => {
        const currentTimeVal = audioElement.currentTime;
        const maxVal = audioElement.duration;
        myProgressBar.value = (currentTimeVal / maxVal) * 100;
        currentTime.innerHTML = formatTime(currentTimeVal);
    }, 1000);
}, 300);


const formatTime = (time) =>{
    let min = Math.floor(time/60);
    if(min<10){
        min = `0${min}`;
    }
    let sec = Math.floor(time%60);
    if(sec<10){
    sec = `0${sec}`;
}

    return `${min}:${sec}`;
}
