var log = function(){
    console.log(arguments)
}

$(document).ready(function(){
    $(".bbs-comment-item").mouseenter(function(){
        cell = $(this).closest($('.bbs-comment-item'))
        menu = $(this).find($('.bbs-comment-menu'))
        menu.removeClass("hidden")
    })
    $(".bbs-comment-item").mouseleave(function(){
        cell = $(this).closest($('.bbs-comment-item'))
        menu = $(this).find($('.bbs-comment-menu'))
        menu.addClass("hidden")
    })
})