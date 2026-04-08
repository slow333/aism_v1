$(function () { 
    const $sidebarItems = $('.col-md-3 .collapse'); 

    function getStoredState() {
        const storedState = localStorage.getItem('sidebarCollapseState');
        return storedState ? JSON.parse(storedState) : []; 
    }

    function saveState(openItems) {
        localStorage.setItem('sidebarCollapseState', JSON.stringify(openItems));
    }

    // 페이지 로드 시 저장된 상태 복원
    const openItems = getStoredState();
    openItems.forEach(function(itemId) {
        const $element = $('#' + itemId); 
        if ($element.length) {
            $element.addClass('show');
            const $button = $(`[data-bs-target="#${itemId}"]`); 
            if ($button.length) { 
                $button.attr('aria-expanded', 'true');
            }
        }
    });

    // collapse 이벤트 리스너를 추가하여 상태 변경 시 저장
    $sidebarItems.each(function () { 
        $(this).on('shown.bs.collapse', function () { 
            let openItems = getStoredState();
            if (!openItems.includes($(this).attr('id'))) { 
                openItems.push($(this).attr('id'));
                saveState(openItems);
            }
        });

        $(this).on('hidden.bs.collapse', function () {
            let openItems = getStoredState();
            const index = openItems.indexOf($(this).attr('id'));
            if (index > -1) {
                openItems.splice(index, 1);
                saveState(openItems);
            }
        });
    });

    // Sidebar show/hide toggle
    const $sidebarToggleBtn = $('#sidebarToggleBtn');
    const $mainCol = $('#mainContentCol');

    function applySidebarState(hidden) {
        if (!$mainCol.length || !$('#sidebarCol').length || !$sidebarToggleBtn.length) return;
        if (hidden) {
            $('#sidebarCol').hide();
            $mainCol.removeClass('col-md-10').addClass('col-md-12');
            $sidebarToggleBtn.attr('aria-expanded', 'false'); 
        } else {
            $('#sidebarCol').show();
            $mainCol.removeClass('col-md-12').addClass('col-md-10');
            $sidebarToggleBtn.attr('aria-expanded', 'true'); 
        }
    }

    // initialize from localStorage
    try {
        const hidden = localStorage.getItem('sidebarHidden') === 'true';
        applySidebarState(hidden);
    } catch (e) {}

    if ($sidebarToggleBtn.length) {
        $sidebarToggleBtn.on('click', function () {
            try {
                const currentlyHidden = localStorage.getItem('sidebarHidden') === 'true';
                const toHide = !currentlyHidden;
                applySidebarState(toHide);
                localStorage.setItem('sidebarHidden', toHide ? 'true' : 'false');
            } catch (e) {
                const isHidden = $('#sidebarCol').is(':hidden');
                applySidebarState(!isHidden);
            }
        });
    }
});
