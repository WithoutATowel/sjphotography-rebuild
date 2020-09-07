$(document).ready(function(){
    $('.modal').modal({
        opacity: 0.9,
        startingTop: '10%'
    });
    $('.sidenav').sidenav();
    $(document).on("keydown", scrollPictures);
    $(document).on("contextmenu", preventImageRightClick);

    function scrollPictures(event) {
        if (event.keyCode && [37, 38, 39, 40].indexOf(event.keyCode) > -1) {
            event.preventDefault();
            var openModal = document.getElementsByClassName("open") ? document.getElementsByClassName("open")[0] : null;
            if (openModal) {
                if (typeof modalImgUrlsArray === 'undefined' || modalImgUrlsArray.indexOf(openModal.getAttribute('src')) === -1) {
                    var modalArray = document.getElementsByClassName("modal");
                    modalImgUrlsArray = Array.prototype.map.call(modalArray, function(item) {
                        return item.getAttribute('src');
                    });
                }
                var currentUrlIndex = modalImgUrlsArray.indexOf(openModal.getAttribute('src'));
                if ([37, 38].indexOf(event.keyCode) > -1 && currentUrlIndex > 0) {
                    // 37 == left arrow, 38 == up arrow
                    currentUrlIndex--;
                    openModal.setAttribute('src', modalImgUrlsArray[currentUrlIndex]);
                } else if ([39, 40].indexOf(event.keyCode) > -1 && currentUrlIndex < (modalImgUrlsArray.length - 1)) {
                    // 39 == right arrow, 40 == down arrow
                    currentUrlIndex++;
                    openModal.setAttribute('src', modalImgUrlsArray[currentUrlIndex]);
                }
            }
            // else the modal isn't open
        }
        // Else the key pressed wasn't an arrow key
    }

    function preventImageRightClick(event) {
        if(event.target.nodeName === 'IMG') {
            console.log('Right clicked an image')
            return false;
        }
    }
});
















