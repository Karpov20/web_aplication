'use strict';
/*Эта функция вызывается, когда пользователь выбирает файл изображения. 
Он считывает выбранный файл изображения с помощью FileReader и отображает предварительный просмотр изображения в указанном элементе 
с помощью класса background-preview > img. 
Если элемент имеет класс d-none (указывающий, что он скрыт), он отображает изображение и скрывает метку.*/
function imagePreviewHandler(event) {
    if (event.target.files && event.target.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            let img = document.querySelector('.background-preview > img');
            img.src = e.target.result;
            if (img.classList.contains('d-none')) {
                let label = document.querySelector('.background-preview > label');
                label.classList.add('d-none');
                img.classList.remove('d-none');
            }
        }
        reader.readAsDataURL(event.target.files[0]);
    }
}
/*эта функция срабатывает при нажатии на элемент внутри карточки (с классом .card), за исключением случаев, когда это элемент BUTTON. 
Он находит ближайший родительский элемент класса .card и проверяет, имеет ли он атрибут data-url. Если это так, он перенаправляет пользователя на указанный URL-адрес.*/
function openLink(event) {
    if (event.target.tagName == 'BUTTON') return;
    let row = event.target.closest('.card');
    if (row.dataset.url) {
        window.location = row.dataset.url;
    }
}



// function deleteBookHandler(event) {  
//     let form = document.querySelector('form');
//     console.log(event.relatedTarget);
//     form.action = event.relatedTarget.dataset.url;
// }
/*Инициализируются два экземпляра редактора EasyMDE. 
Один для элемента с идентификатором text_review и другой для элемента с идентификатором short_desc. EasyMDE — редактор JavaScript Markdown. */
let textReview = document.getElementById('text_review')
if (textReview) {
    const easymde = new EasyMDE({textReview},);
}

let shortDesk = document.getElementById('short_desc')
if (shortDesk) {
    const easymde = new EasyMDE({shortDesk},);
}
/*Функция imagePreviewHandler срабатывает, когда пользователь выбирает изображение, используя указанное поле ввода файла (если оно существует).
Функция openLink срабатывает при нажатии на любой элемент класса .card внутри .books-list (за исключением элементов BUTTON).*/
window.onload = function() {
    // let deleteModal = document.querySelector('#delete');
    // if (deleteModal) {
    //     deleteModal.addEventListener('show.bs.modal', deleteBookHandler)
    // }
    let background_img_field = document.getElementById('background_img');
    if (background_img_field) {
        background_img_field.onchange = imagePreviewHandler;
    }
    for (let course_elm of document.querySelectorAll('.books-list .card')) {
        course_elm.onclick = openLink;
    }
}