console.log('подключили js')
let tagTemplateSubModal=document.querySelector('#template-sub-modal');
let modalWrapper=document.querySelector('.modal__wrapper');
let templateSubModal=tagTemplateSubModal.content.cloneNode(true);
let spanOpenSubModal=modalWrapper.querySelector('.open-sub-modal');

spanOpenSubModal.addEventListener('click', ()=>{
    console.log('ddddddddddddddddd');
    modalWrapper.append(templateSubModal);
    let subModalWrapper=document.querySelector('.sub-modal__wrapper');
    subModalWrapper.classList.add('modal__wrapper_visible');
    let subModalClose= subModalWrapper.querySelector('.modal__close');
        subModalWrapper.addEventListener('click', (event)=>{
            event.stopPropagation();
            if ((event.target == subModalWrapper) || (event.target == subModalClose)) {
                subModalWrapper.classList.remove('modal__wrapper_visible');
            };
           
        })
})

