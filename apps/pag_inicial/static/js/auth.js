document.querySelectorAll('.role-card').forEach(button => {
  button.addEventListener('click', () => {
    const role = button.getAttribute('data-role');

    // Esconde a tela de seleção de papel
    document.getElementById('role-selection-screen').classList.add('d-none');

    // Esconde todas as telas de formulário
    document.querySelectorAll('.auth-form-screen').forEach(screen => screen.classList.add('d-none'));

    // Mostra a tela do formulário correspondente
    document.getElementById(`${role}-form-screen`).classList.remove('d-none');
  });
});

// Botões “Voltar” para retornar à seleção de papel
document.querySelectorAll('.back-to-selection').forEach(button => {
  button.addEventListener('click', () => {
    // Esconde todas as telas de formulário
    document.querySelectorAll('.auth-form-screen').forEach(screen => screen.classList.add('d-none'));

    // Mostra a tela de seleção de papel
    document.getElementById('role-selection-screen').classList.remove('d-none');
  });
});
