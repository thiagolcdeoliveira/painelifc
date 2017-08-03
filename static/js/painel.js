function turma_pesquisar(n) {
    var select_turma = $("select#id_turma"+n).val();
    var select_autor = $("select#id_autor"+n);
    if (select_turma != "select") {
        $.ajax({
            type: 'GET',
            url: '/cadastro-trabalho/',
            data: {
                turma_id: select_turma,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var alunos = "";
                for (var i = 0; i < data.length; i++) {
                    alunos += '<option value="' + data[i]['id'] + '">' + data[i]['nome'] + '</option>';
                }
                select_autor.html(alunos);
                $("#id_autor_field > .selection.ui.dropdown > .text").html("Selecione um autor");
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}