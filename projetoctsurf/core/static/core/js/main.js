// Aguardar o carregamento completo do DOM
document.addEventListener('DOMContentLoaded', function() {
    
    // ========================================
    // FUNCIONALIDADE DO MENU DROPDOWN
    // ========================================
    const menuToggles = document.querySelectorAll('.menu-toggle');
    
    menuToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            
            const menuItem = this.parentElement;
            const isActive = menuItem.classList.contains('active');
            
            // Fechar todos os outros menus
            document.querySelectorAll('.menu-item').forEach(item => {
                if (item !== menuItem) {
                    item.classList.remove('active');
                }
            });
            
            // Alternar o menu atual
            if (isActive) {
                menuItem.classList.remove('active');
            } else {
                menuItem.classList.add('active');
            }
        });
    });
    
    // ========================================
    // MANTER MENU ABERTO NA PÁGINA ATUAL
    // ========================================
    const currentPath = window.location.pathname;
    document.querySelectorAll('.submenu a').forEach(link => {
        const linkPath = link.getAttribute('href');
        
        // Verifica se é a página atual
        if (linkPath && linkPath === currentPath) {
            link.classList.add('active');
            
            // Abre o menu pai
            const menuItem = link.closest('.menu-item');
            if (menuItem) {
                menuItem.classList.add('active');
            }
        }
    });
    
    // ========================================
    // CONFIRMAÇÃO DE EXCLUSÃO
    // ========================================
    const deleteLinks = document.querySelectorAll('.action-icon.icon-delete, [data-confirm]');
    
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const message = this.getAttribute('data-confirm') || 'Tem certeza que deseja excluir este item?';
            
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });
    
    // ========================================
    // AUTO-FECHAR MENSAGENS DE ALERTA
    // ========================================
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        // Adicionar botão de fechar
        const closeBtn = document.createElement('span');
        closeBtn.innerHTML = '×';
        closeBtn.style.cssText = 'cursor: pointer; float: right; font-size: 1.5em; line-height: 0.8;';
        closeBtn.addEventListener('click', function() {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        });
        alert.insertBefore(closeBtn, alert.firstChild);
        
        // Auto-fechar após 5 segundos
        setTimeout(() => {
            alert.style.transition = 'opacity 0.3s ease';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
    
    // ========================================
    // PREVIEW DE IMAGEM NO UPLOAD
    // ========================================
    const fileInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
    
    fileInputs.forEach(input => {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                
                reader.onload = function(event) {
                    // Procurar por preview existente ou criar um novo
                    let preview = input.parentElement.querySelector('.image-preview');
                    
                    if (!preview) {
                        preview = document.createElement('div');
                        preview.className = 'image-preview';
                        input.parentElement.appendChild(preview);
                    }
                    
                    preview.innerHTML = `
                        <img src="${event.target.result}" alt="Preview">
                        <p>Nova imagem selecionada</p>
                    `;
                };
                
                reader.readAsDataURL(file);
            }
        });
    });
    
    // ========================================
    // ANIMAÇÃO DE LOADING NOS BOTÕES DE SUBMIT
    // ========================================
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            
            if (submitBtn && !submitBtn.classList.contains('loading')) {
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
            }
        });
    });
    
    // ========================================
    // CONTADOR DE CARACTERES PARA TEXTAREA
    // ========================================
    const textareas = document.querySelectorAll('textarea[maxlength]');
    
    textareas.forEach(textarea => {
        const maxLength = textarea.getAttribute('maxlength');
        
        if (maxLength) {
            // Criar elemento contador
            const counter = document.createElement('div');
            counter.className = 'char-counter';
            textarea.parentElement.appendChild(counter);
            
            // Função para atualizar contador
            const updateCounter = () => {
                const currentLength = textarea.value.length;
                const remaining = maxLength - currentLength;
                
                counter.textContent = `${currentLength} / ${maxLength} caracteres`;
                
                // Adicionar classes de aviso
                counter.classList.remove('warning', 'danger');
                if (remaining < 50) {
                    counter.classList.add('warning');
                }
                if (remaining < 20) {
                    counter.classList.add('danger');
                }
            };
            
            // Atualizar ao digitar
            textarea.addEventListener('input', updateCounter);
            
            // Atualizar no carregamento
            updateCounter();
        }
    });
    
    // ========================================
    // SCROLL SUAVE PARA ÂNCORAS
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href !== '#' && href !== '') {
                e.preventDefault();
                const target = document.querySelector(href);
                
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // ========================================
    // MENSAGEM DE CONFIRMAÇÃO AO SAIR COM ALTERAÇÕES
    // ========================================
    let formChanged = false;
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        
        inputs.forEach(input => {
            input.addEventListener('change', function() {
                formChanged = true;
            });
        });
        
        form.addEventListener('submit', function() {
            formChanged = false;
        });
    });
    
    window.addEventListener('beforeunload', function(e) {
        if (formChanged) {
            e.preventDefault();
            e.returnValue = 'Você tem alterações não salvas. Deseja realmente sair?';
            return e.returnValue;
        }
    });
    
});

// ========================================
// FUNÇÕES AUXILIARES GLOBAIS
// ========================================

// Mostrar notificação toast (pode ser usada em qualquer lugar)
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    toast.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        background: ${type === 'success' ? '#28a745' : type === 'error' ? '#dc3545' : '#17a2b8'};
        color: white;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        z-index: 9999;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Adicionar animação CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);
