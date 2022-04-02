// Table functionality on student view

$(document).ready( function () {
    $('#datatable_students').DataTable({
        paging: false,
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'collection',
                text: 'Student Info',
                className: 'customn-html-collection',
                buttons: [
                    {
                        extend: 'colvisGroup',
                        text: 'All Instrumentation',
                        show: [ 0, 1, 2, 3, 4, 15 ],
                        hide: [ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Concert Band Instrumentation',
                        show: [ 0, 1, 2, 15 ],
                        hide: [ 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Marching Band Instrumentation',
                        show: [ 0, 1, 3, 15 ],
                        hide: [ 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Jazz Band Instrumentation',
                        show: [ 0, 1, 4, 15 ],
                        hide: [ 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'School Owned Instruments',
                        show: [ 0, 1, 13, 14, 15 ],
                        hide: [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Concert Uniforms',
                        show: [ 0, 1, 5, 6, 7, 15 ],
                        hide: [ 2, 3, 4, 8, 9, 10, 11, 12, 13, 14 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Marching Uniforms',
                        show: [ 0, 1, 8, 9, 10, 11, 12, 15 ],
                        hide: [ 2, 3, 4, 5, 6, 7, 13, 14 ]
                    },
                    {
                        extend: 'colvisGroup',
                        text: 'Student Names',
                        show: [ 0, 1, 15 ],
                        hide: [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]
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
                targets: [ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ],
                visible: false,
            },
        ]
    });
});

// Table functionality for accounts

$(document).ready( function () {
    $('#datatable_accounts, #datatable_library').DataTable({
        paging: false,
        // bInfo: false,
        // ordering: false,
        dom: 'Bfrtip',
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
});

// go back button
function goBack() {
    window.history.back();
}