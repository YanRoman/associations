'use strict'

const list = document.querySelector('.list');
async function getProducts(){
    console.log('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Build Products');
    list.innerHTML = ``
    let temp = await eel.getProducts()();
    temp.forEach(element => {
        console.log(element);
        list.innerHTML += `<li><button class="btn">${element}</button></li>`
    });
}

const droparea = document.querySelector('.droparea');
const svg_dropadrea = document.querySelector('.svg_droparea');

droparea.addEventListener("dragover", (e) => {
    e.preventDefault();
    droparea.classList.add("hover");
    svg_dropadrea.classList.add("svg_hover");
});

droparea.addEventListener("dragleave", () => {
    droparea.classList.remove("hover");
    svg_dropadrea.classList.remove("svg_hover");
});

droparea.addEventListener("drop", (e) => {
    e.preventDefault();

    const file = e.dataTransfer.files[0];
    const type = file.type;
    console.log(type);

    if(type=="text/plain"){
        return upload(file);
    } else{
        droparea.setAttribute("class", "droparea invalid");
        droparea.innerText = "Invalid file format";
        return false;
    }
});

const upload = (file) => {
    getProducts();
    buildRulesTable();
    let reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function(){
        let data = reader.result;
        send(data);
    }    
    reader.onerror = function(){
        console.log(reader.error);
    }
    document.querySelector('.main').style.display = 'none';
    document.querySelector('.results').style.display = 'flex';
};

async function send(data){
    await eel.take_py(data)();
}

//-------------------------------------------------------ADD-FILE

const rulesBtn = querySelector('.rules-btn');
rulesBtn.addEventListener('click', e=>{
    rulesTable.style.display = 'block';
    // tree
    //if-else
})

const rulesTable = document.querySelector('.rules-table-body');
async function buildRulesTable(){
    rulesTable.innerHTML = ``
    var info = []
    info = await eel.getInfo()();
    console.log(info);
    let i = 0
    info.forEach(e => {
        rulesTable.innerHTML += `<tr><td>${i}</td><td>${e[0]}</td><td>${e[1]}</td><td>${e[2]}</td><td>${e[3]}</td><td>${e[4]}</td></tr>`
        i++;
    });
    // await eel.getInfo()().forEach(e =>{
    //     rulesTable.innerHTML += `<tr><td>${e[0]}</td><td>${e[1]}</td><td>${e[2]}</td><td>${e[3]}</td><td>${e[4]}</td><td>${e[5]}</td></tr>`
    // });
}