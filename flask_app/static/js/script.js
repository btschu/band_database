// Table functionality on student view

$(document).ready( function () {
    $('#datatable_students').DataTable({
        // fixedHeader: true,
        // lengthMenu: [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
        // responsive: true,
        dom: 't',
        scrollCollapse: true,
        fixedColumns: true,
        paging: false,
        autoWidth: false,
        scrollY: '45vh',
        scrollX: true,
        dom: 'Blfrtip',
        autoHeight: false,
        language:{
            // search: "<i class='fa fa-search'></i>",
            search: "",
            searchPlaceholder: "Search...",
        },
        buttons: [
            {
                extend: 'collection',
                text: 'Student Info',
                className: 'custom-html-collection',
                buttons: [
                    {
                        extend: 'colvisGroup',
                        text: 'Student Names (SORT)',
                        show: [ 1, 2, 18 ],
                        hide: [ 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'All Information',
                        show: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ],
                        // hide: [ 1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'All Instrumentation',
                        show: [ 0, 3, 4, 5, 18 ],
                        hide: [ 1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Concert Band Instrumentation',
                        show: [ 0, 3, 18 ],
                        hide: [ 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Marching Band Instrumentation',
                        show: [ 0, 4, 18 ],
                        hide: [ 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Jazz Band Instrumentation',
                        show: [ 0, 5, 18 ],
                        hide: [ 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'School Owned Instruments',
                        show: [ 0, 16, 17, 18 ],
                        hide: [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Concert Uniforms',
                        show: [ 0, 6, 7, 8, 9, 18 ],
                        hide: [ 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Marching Uniforms',
                        show: [ 0, 10, 11, 12, 13, 14, 15, 18 ],
                        hide: [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 17 ]
                    },
                ]
            },
            'colvis',
            {
                extend: 'collection',
                text: 'Export',
                className: 'custom-html-collection',
                buttons: [
                    {
                        extend: 'copy',
                        exportOptions: {
                            columns: [':visible :not(:last-child)']
                        }
                    },
                    {
                        extend: 'excel',
                        exportOptions: {
                            columns: [':visible :not(:last-child)']
                        }
                    },
                    {
                        extend: 'pdf',
                        exportOptions: {
                            columns: [':visible :not(:last-child)']
                        }
                    },
                    {
                        extend: 'print',
                        exportOptions: {
                            columns:  [':visible :not(:last-child)']
                        }
                    }
                ]
            },
        ],
        // columnDefs: [
        //     {
        //         targets: [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ],
        //         visible: false,
        //     },
        // ]
    });
    new $.fn.dataTable.FixedHeader( table );
});

// Table functionality for accounts

$(document).ready( function () {
    $('#datatable_accounts, #datatable_library').DataTable({
        paging: false,
        fixedHeader: true,
        // autoWidth: false,
        // scrollY: '50vh',
        // scrollX: '50vh',
        // scrollCollapse: true,
        // lengthMenu: [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
        // bInfo: false,
        // ordering: false,
        dom: 'Blfrtip',
        responsive: true,
        language:{
            // search: "<i class='fa fa-search'></i>",
            search: "",
            searchPlaceholder: "Search...",
        },
        buttons: [
            'colvis',
            {
                extend: 'collection',
                text: 'Export',
                className: 'custom-html-collection',
                buttons: [
                    {
                        extend: 'copy',
                        exportOptions: {
                            columns: [':visible :not(:last-child)']
                        }
                    },
                    {
                        extend: 'excel',
                        exportOptions: {
                            columns: [':visible :not(:last-child)']
                        }
                    },
                    {
                        extend: 'pdf',
                        exportOptions: {
                            columns: [':visible :not(:last-child)']
                        }
                    },
                    {
                        extend: 'print',
                        exportOptions: {
                            columns:  [':visible :not(:last-child)']
                        }
                    },
                ]
            },
        ],
    });
    new $.fn.dataTable.FixedHeader( table );
});

// go back button
function goBack() {
    window.history.back();
}