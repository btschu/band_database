// Table functionality on everything except viewing accounts

$(document).ready( function () {
    $('#datatablesSimple').DataTable({
        paging: false,
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'colvisGroup',
                text: 'Student Names',
                show: [ 0, 1, 13 ],
                hide: [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
            },
            {
                extend: 'colvisGroup',
                text: 'Instrument Info',
                show: [ 0, 1, 2, 3, 4, 13 ],
                hide: [ 5, 6, 7, 8, 9, 10, 11, 12 ]
            },
            {
                extend: 'colvisGroup',
                text: 'Concert Uniforms',
                show: [ 0, 1, 5, 6, 7, 13 ],
                hide: [ 2, 3, 4, 8, 9, 10, 11, 12 ]
            },
            {
                extend: 'colvisGroup',
                text: 'Marching Uniforms',
                show: [ 0, 1, 8, 9, 10, 11, 12, 13 ],
                hide: [ 2, 3, 4, 5, 6, 7 ]
            },
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
                    // {
                    //     extend: 'csv',
                    //     exportOptions: {
                    //         columns: [':visible :not(:last-child)']
                    //     }
                    // },
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
            // 'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        columnDefs: [
            {
                targets: [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ],
                visible: false,
            },
        ]
    });
});

// Table functionality for accounts

$(document).ready( function () {
    $('#datatablesSimple2').DataTable({
        paging: false,
        dom: 'Bfrtip',
        buttons: [
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
                    // {
                    //     extend: 'csv',
                    //     exportOptions: {
                    //         columns: [':visible :not(:last-child)']
                    //     }
                    // },
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
            // 'copy', 'csv', 'excel', 'pdf', 'print'
        ],
    });
});

// go back button
function goBack() {
    window.history.back();
}

// $(document).ready(function(){
//     var table = $('#datatablesSimple').DataTable();
//        //DataTable custom search field
//         $('#custom-filter').keyup( function() {
//           table.search( this.value ).draw();
//         } );
//     });

// get sum of columns on view one account
// $(document).ready(function() {
//     $('#datatablesSimple').dataTable({
//     	"footerCallback": function ( row, data, start, end, display ) {
//             var api = this.api(), data;
 
//             // converting to interger to find total
//             var intVal = function ( i ) {
//                 return typeof i === 'string' ?
//                     i.replace(/[\$,]/g, '')*1 :
//                     typeof i === 'number' ?
//                         i : 0;
//             };

//             // computing column Total of the complete result
//             var item_cost = api
//                 .column( 3 )
//                 .data()
//                 .reduce( function (a, b) {
//                     return intVal(a) + intVal(b);
//                 }, 0 );

// 	        var item_payment = api
//                 .column( 4 )
//                 .data()
//                 .reduce( function (a, b) {
//                     return intVal(a) + intVal(b);
//                 }, 0 );

// 	        var total_owed = api
//                 .column( 5 )
//                 .data()
//                 .reduce( function (a, b) {
//                     return intVal(a) + intVal(b);
//                 }, 0 );
			
				
//             // Update footer by showing the total with the reference of the column index 
// 	    $( api.column( 0 ).footer() ).html('Total');
//             $( api.column( 3 ).footer() ).html(item_cost);
//             $( api.column( 4 ).footer() ).html(item_payment);
//             $( api.column( 5 ).footer() ).html(total_owed);
//         },
//         "processing": true,
//         "serverSide": true,
//         "ajax": "server.php"
//     } );
// } );