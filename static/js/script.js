function iniciarJornada() {
    const lavadores = [
        document.getElementById('lavador-1').value,
        document.getElementById('lavador-2').value,
        document.getElementById('lavador-3').value,
    ];

    const vehicle = {
        tipo: document.getElementById('car-type').value,
        color: document.getElementById('car-color').value,
        licencia: document.getElementById('license-number').value
    };

    const vehiculosList = document.getElementById('vehiculos-list');
    const newVehicleEntry = document.createElement('div');
    newVehicleEntry.textContent = Vehículo: ${vehicle.tipo}; Color: ${vehicle.color}; Licencia: ${vehicle.licencia};
    vehiculosList.appendChild(newVehicleEntry);

    console.log("Iniciando jornada con los lavadores:", lavadores);
}

function finalizarJornada() {
    alert('Jornada finalizada.');
    // Aquí puedes agregar más lógica para finalizar la jornada
}

function verVehiculos() {
    alert('Aquí se mostrarán los vehículos lavados.');
}

function ajustes() {
    alert('Aquí se realizarán los ajustes necesarios.');
}