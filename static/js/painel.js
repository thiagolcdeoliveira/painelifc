function turma_pesquisar() {
    $.ajax({
        type: 'GET',
        url: '/cadastro-trabalho/',
        data: {
            turma_id: $("select[name='turma']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            // console.log(data);
            var alunos = '';
            for (var i = 0; i < data.length; i++) {
                alunos += '<option value="' + data[i]['id'] + '">' + data[i]['nome'] + '</option>';
            }
            $("#id_autor_select").html(alunos);
            // $("#id_autor_select").attr('disabled', false);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}
