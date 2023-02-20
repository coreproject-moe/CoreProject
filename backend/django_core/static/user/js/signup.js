const el = document.querySelector('#id_username');

el.addEventListener('input', () => {
    const value = el.value;

    const HashLength = value.match(/#/gi).length;

    if (HashLength === 1) {
        console.log(1);
    }else{
        
    }
});
