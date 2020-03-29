$(".shop-now").click(function () {
    var targetId = $(this).attr('data-id');
    $('html, body').animate({
        scrollTop: $('#' + targetId).offset().top
    }, 2000);
});

$(".book-list").click(function () {
    var targetId = $(this).attr('data-target');
    $('html, body').animate({
        scrollTop: $('#' + targetId).offset().top
    }, 2000);
});