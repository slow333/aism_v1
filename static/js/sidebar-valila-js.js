document.addEventListener('DOMContentLoaded', function () {
$(function () { // jQuery equivalent of DOMContentLoaded
    // 사이드바의 collapse 요소들을 가져옵니다.
    const sidebarCollapses = document.querySelectorAll('.col-md-3 .collapse');
    const $sidebarCollapses = $('.col-md-3 .collapse'); // Use jQuery selector
    const storageKey = 'sidebarCollapseState';

    // localStorage에서 현재 상태를 가져오는 함수
    function getStoredState() {
        const storedState = localStorage.getItem(storageKey);
        return storedState ? JSON.parse(storedState) : [];
        return storedState ? JSON.parse(storedState) : []; // localStorage methods remain the same
    }

    // localStorage에 상태를 저장하는 함수
    function saveState(openItems) {
        localStorage.setItem(storageKey, JSON.stringify(openItems));
        localStorage.setItem(storageKey, JSON.stringify(openItems)); // localStorage methods remain the same
    }

    // 페이지 로드 시 저장된 상태 복원
    const openItems = getStoredState();
    openItems.forEach(function(itemId) {
        const element = document.getElementById(itemId);
        if (element) {
            element.classList.add('show');
            const button = document.querySelector(`[data-bs-target="#${itemId}"]`);
            if (button) {
                button.setAttribute('aria-expanded', 'true');
        const $element = $('#' + itemId); // Use jQuery selector
        if ($element.length) { // Check if element exists
            $element.addClass('show'); // Use jQuery addClass
            const $button = $(`[data-bs-target="#${itemId}"]`); // Use jQuery selector
            if ($button.length) { // Check if button exists
                $button.attr('aria-expanded', 'true'); // Use jQuery attr
            }
        }
    });

    // collapse 이벤트 리스너를 추가하여 상태 변경 시 저장
    sidebarCollapses.forEach(function (collapseEl) {
        collapseEl.addEventListener('shown.bs.collapse', function () {
    $sidebarCollapses.each(function () { // Use jQuery each for iteration
        const $collapseEl = $(this); // Cache jQuery object for current collapse element
        $collapseEl.on('shown.bs.collapse', function () { // Use jQuery on for event listener
            let openItems = getStoredState();
            if (!openItems.includes(this.id)) {
                openItems.push(this.id);
            if (!openItems.includes($collapseEl.attr('id'))) { // Get ID using jQuery attr
                openItems.push($collapseEl.attr('id'));
                saveState(openItems);
            }
        });

        collapseEl.addEventListener('hidden.bs.collapse', function () {
        $collapseEl.on('hidden.bs.collapse', function () { // Use jQuery on for event listener
            let openItems = getStoredState();
            const index = openItems.indexOf(this.id);
            const index = openItems.indexOf($collapseEl.attr('id')); // Get ID using jQuery attr
            if (index > -1) {
                openItems.splice(index, 1);
                saveState(openItems);
            }
        });
    });

    // Sidebar show/hide toggle
    const sidebarToggleBtn = document.getElementById('sidebarToggleBtn');
    const mainCol = document.getElementById('mainContentCol');
    const sidebarCol = document.getElementById('sidebarCol');
    const $sidebarToggleBtn = $('#sidebarToggleBtn'); // Use jQuery selector
    const $mainCol = $('#mainContentCol'); // Use jQuery selector
    const $sidebarCol = $('#sidebarCol'); // Use jQuery selector
    const storageKeyHidden = 'sidebarHidden';

    function applySidebarState(hidden) {
        if (!mainCol || !sidebarCol || !sidebarToggleBtn) return;
        if (!$mainCol.length || !$sidebarCol.length || !$sidebarToggleBtn.length) return; // Check if elements exist using .length
        if (hidden) {
            sidebarCol.style.display = 'none';
            mainCol.classList.remove('col-md-10');
            mainCol.classList.add('col-md-12');
            sidebarToggleBtn.setAttribute('aria-expanded', 'false');
            $sidebarCol.hide(); // Use jQuery hide()
            $mainCol.removeClass('col-md-10').addClass('col-md-12'); // Use jQuery removeClass/addClass chaining
            $sidebarToggleBtn.attr('aria-expanded', 'false'); // Use jQuery attr
        } else {
            sidebarCol.style.display = '';
            mainCol.classList.remove('col-md-12');
            mainCol.classList.add('col-md-10');
            sidebarToggleBtn.setAttribute('aria-expanded', 'true');
            $sidebarCol.show(); // Use jQuery show()
            $mainCol.removeClass('col-md-12').addClass('col-md-10'); // Use jQuery removeClass/addClass chaining
            $sidebarToggleBtn.attr('aria-expanded', 'true'); // Use jQuery attr
        }
    }

    // initialize from localStorage
    try {
        const hidden = localStorage.getItem(storageKeyHidden) === 'true';
        applySidebarState(hidden);
        applySidebarState(hidden); // localStorage methods remain the same
    } catch (e) {}

    if (sidebarToggleBtn) {
        sidebarToggleBtn.addEventListener('click', function () {
    if ($sidebarToggleBtn.length) { // Check if button exists
        $sidebarToggleBtn.on('click', function () { // Use jQuery on for event listener
            try {
                const currentlyHidden = localStorage.getItem(storageKeyHidden) === 'true';
                const toHide = !currentlyHidden;
                applySidebarState(toHide);
                localStorage.setItem(storageKeyHidden, toHide ? 'true' : 'false');
                applySidebarState(toHide); // localStorage methods remain the same
                localStorage.setItem(storageKeyHidden, toHide ? 'true' : 'false'); // localStorage methods remain the same
            } catch (e) {
                // fallback toggle
                const isHidden = sidebarCol.style.display === 'none';
                // Fallback using jQuery's :hidden selector or checking display
                const isHidden = $sidebarCol.is(':hidden'); // Use jQuery is(':hidden')
                applySidebarState(!isHidden);
            }
        });
    }
});
