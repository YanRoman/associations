'use strict'

//-------------------------------------------------------DROPDOWN-MENU
const list = document.querySelector('.dropdown-menu');
const unload = document.querySelector('.unload');
async function getProducts(){
    list.innerHTML = ``
    let products = await eel.getProducts()();
    products.forEach((item) => {
        list.innerHTML += `<li><button class="btn dropdown-item">${item}</button></li>`
    })
}

unload.addEventListener('click', () => {
    console.log("unload");
    getProducts();
})


document.querySelectorAll('.dropdown-toggle').forEach(e => {
    e.addEventListener('click', e => {
        const menu = e.currentTarget.dataset.path;
        document.querySelectorAll('.dropdown-menu').forEach(e => {
            if(!document.querySelector(`[data-target=${menu}]`).classList.contains('open')){
                document.querySelector(`[data-target=${menu}]`).classList.add('menu-active');
                setTimeout(() => {
                    document.querySelector(`[data-target=${menu}]`).classList.add('open')
                }, 0);
            }
 
            if(document.querySelector(`[data-target=${menu}]`).classList.contains('open')){
                document.querySelector(`[data-target=${menu}]`).classList.remove('menu-active');
                setTimeout(() => {
                    document.querySelector(`[data-target=${menu}]`).classList.remove('open')
                }, 0);
            }
        });
    });
});
//-------------------------------------------------------DROPDOWN-MENU

//-------------------------------------------------------ADD-FILE
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
    droparea.setAttribute("class", "droparea valid");
    // droparea.innerText = "added " + file.name;
    document.querySelector(".newfile").style.display = "none";
    document.querySelector(".file").style.display = "block";

    let reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function(){
        let data = reader.result;
        send(data);
    }    
    reader.onerror = function(){
        console.log(reader.error);
    }
};

async function send(data){
    await eel.take_py(data)();
}

//-------------------------------------------------------ADD-FILE
