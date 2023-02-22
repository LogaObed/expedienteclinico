function solicitud() {
    foms.innerHTML = `
    <form action="{% url 'nuevopaciente' %}" method="post">
        <h1 class="text-center">Formulario de registro</h1>
        {% csrf_token %}
        {{form}}
         <button type="submit" class="btn btn-success">Insertar </button>
     </form>
    `;
}

function consultapaciente() {
    alert('paciente');
}

function consultapersonal() {
    alert('personal');
}

function consultacontacto() {
    alert('contacto');
}