function loadStudents() {
    let name = $('#nameFilter').val();
    $.get('/students', { name: name }, function(data) {
        $('#students').empty();
        data.forEach(function(student) {
            $('#students').append(`
                <div>
                    <h3>${student.name} (вік: ${student.age})</h3>
                    <p>Курс: ${student.course}</p>
                    <img src="${student.photo_url}" width="100">
                    <hr>
                </div>
            `);
        });
    });
}
