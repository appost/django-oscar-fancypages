  //Reset carousels dependant on container width
function resetCarousel() {
  $('.es-carousel-wrapper').each(function () {
    var es_carouselWidth = $(this).closest('.widget-wrapper').width();
    if (es_carouselWidth > 300) {
      $(this).elastislide({
        minItems: 4,
        onClick: true
      });
    } else {
      $(this).elastislide({
        minItems: 1,
        onClick: true
      });
    }   
  });
}
// initialise fitVids plugin for resizing IFRAME YouTube videos
function initFitvids() {
  $('.widget-video').fitVids();
}

$(document).ready(function() {
    resetCarousel();
    initFitvids();    
});