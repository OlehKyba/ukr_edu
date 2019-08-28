

const spanFileName = document.getElementById("fileName");

const inputImageFile = document.getElementById("inputImageFile");

const inputDate = document.getElementById("inputDate");


const getToday = () => {
    const today = new Date();
    return today.toISOString().substr(0, 10);
};


inputImageFile.addEventListener('input', () => (spanFileName.innerHTML = inputImageFile.value, console.log(inputImageFile.value)));
inputDate.value = inputDate.value ? inputDate.value : getToday();



