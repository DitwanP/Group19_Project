$(".shop-now").click(function () {
    var targetId = $(this).attr('data-id');
    $('html, body').animate({
        scrollTop: $('#' + targetId).offset().top
    }, 2000);
});

// $(".book-list").click(function () {
//     var targetId = $(this).attr('data-target');
//     if (window.location.search.length > 0) {
//         window.location = window.location.origin + '#' + targetId;
//     }
//
//     $('html, body').animate({
//         scrollTop: $('#' + targetId).offset().top
//     }, 2000);
// });


$('#sorter').change(function () {
    var data = {"sort_type": $(this).val(), "page_url": window.location.pathname};
    var urlParams = new URLSearchParams(window.location.search);

    if (urlParams.has('page')) {
        data['page'] = urlParams.get('page');
    }

    $.ajax({
        type: "GET",
        url: BASEURL + "filter-data/",
        data: data,
        async: false,
        success: function (response) {
            $("#tab_content_book").html(response);
        },
        error: function () {
            alert('Error occured');
        }
    });
});

$('#sorter_released').change(function () {
    var data = {"sort_type": $(this).val(), "page_url": window.location.pathname};
    var urlParams = new URLSearchParams(window.location.search);

    if (urlParams.has('page')) {
        data['page'] = urlParams.get('page');
    }

    $.ajax({
        type: "GET",
        url: BASEURL + "filter-released-data/",
        data: data,
        async: false,
        success: function (response) {
            $("#tab_content_book").html(response);
        },
        error: function () {
            alert('Error occured');
        }
    });
});

$('.book-details').click(function (e) {
    var bookId = $(this).attr('data-id');

    if (bookId > 0) {
        var data = {"book_id": bookId};
        $.ajax({
            type: "GET",
            url: BASEURL + "get-book-details/",
            data: data,
            async: false,
            success: function (response) {
                $("#book_details").html(response);
            },
            error: function () {
                alert('Error occured');
            }
        });
    }
});