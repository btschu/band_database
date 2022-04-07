// Table functionality on student view

$(document).ready( function () {
    $('#datatable_students').DataTable({
        paging: false,
        // scrollY: '50vh',
        // scrollX: '50vh',
        // scrollCollapse: true,
        // lengthMenu: [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
        dom: 'Blfrtip',
        autoHeight: false,
        // responsive: true,
        buttons: [
            {
                extend: 'collection',
                text: 'Student Info',
                className: 'customn-html-collection',
                buttons: [
                    {
                        extend: 'colvisGroup',
                        text: 'All Instrumentation',
                        show: [ 0, 1, 2, 3, 4, 17 ],
                        hide: [ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Concert Band Instrumentation',
                        show: [ 0, 1, 2, 17 ],
                        hide: [ 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Marching Band Instrumentation',
                        show: [ 0, 1, 3, 17 ],
                        hide: [ 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Jazz Band Instrumentation',
                        show: [ 0, 1, 4, 17 ],
                        hide: [ 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'School Owned Instruments',
                        show: [ 0, 1, 15, 16, 17 ],
                        hide: [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Concert Uniforms',
                        show: [ 0, 1, 5, 6, 7, 8, 17 ],
                        hide: [ 2, 3, 4, 9, 10, 11, 12, 13, 14, 15, 16 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Marching Uniforms',
                        show: [ 0, 1, 9, 10, 11, 12, 13, 14, 17 ],
                        hide: [ 2, 3, 4, 5, 6, 7, 8, 15, 16 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Student Names',
                        show: [ 0, 1, 17 ],
                        hide: [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]
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
        columnDefs: [
            {
                targets: [ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ],
                visible: false,
            },
        ]
    });
    new $.fn.dataTable.FixedHeader( table );
});

// Table functionality for accounts

$(document).ready( function () {
    $('#datatable_accounts, #datatable_library').DataTable({
        paging: false,
        // scrollY: '50vh',
        // scrollX: '50vh',
        // scrollCollapse: true,
        // lengthMenu: [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
        // bInfo: false,
        // ordering: false,
        dom: 'Blfrtip',
        // responsive: true,
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