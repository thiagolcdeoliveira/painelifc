/**
 * Created by iago on 24/08/16.
 */
$(document).ready(function () {
    $('select').dropdown({});

    $('.message .close')
        .on('click', function () {
            $(this)
                .closest('.message')
                .transition('fade')
            ;
        })
    ;
});