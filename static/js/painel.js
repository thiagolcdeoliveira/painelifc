function turma_pesquisar() {
    var select_turma = $("select[name='turma']").val();
    var select_autor = $("select#id_autor_select");
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
                // console.log(data);
                var alunos = "<option value='select'>Selecione um autor</option>";
                for (var i = 0; i < data.length; i++) {
                    alunos += '<option value="' + data[i]['id'] + '">' + data[i]['nome'] + '</option>';
                }
                select_autor.html(alunos);
                select_autor.prop('disabled', false);
                $("#id_autor_field > .selection.ui.dropdown.disabled").removeClass("disabled");
                $("#id_autor_field > .selection.ui.dropdown > .text").html("Seleicone um autor");
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    } else {
        select_autor.html("<option value='select'>Seleicone uma turma primeiro</option>");
        $("#id_autor_field > .selection.ui.dropdown > .text").html("Seleicone uma turma primeiro");
        select_autor.prop('disabled', true);
        $("#id_autor_field > .selection.ui.dropdown").addClass("disabled");
    }
}
