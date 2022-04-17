
$.datetimepicker.setLocale("zh-TW");
    $('#picker_start').datetimepicker({
        timepicker: false,
        datepicker: true,
        format: 'Y/m/d',
        value: '2021/01/01',
    })
    $('#picker_end').datetimepicker({
        timepicker: false,
        datepicker: true,
        format: 'Y/m/d',
        value: '2021/12/31'
    })
