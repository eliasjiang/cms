layui.use(['table', 'form', 'layer'], function () {
    var table = layui.table;
    var form = layui.form;
    var layer = layui.layer;


    table.render({
        elem: '#category-table',
        url: '/admin/categories',
        title: '分类列表',
        id: 'filter-category-table',
        cols: [[
            {field: 'id', title: 'ID', width: '10%', unresize: true, sort: true},
            // {field: 'parentid', title: '父分类', width: '20%', edit: 'text'},
            {field: 'name', title: '分类名称', width: '20%'},
            {field: 'slug', title: '分类别名', width: '20%'},
            {field: 'description', title: '分类描述'},
            {field: 'operation', title: '操作', toolbar: '#toolbar-category', width: '15%'}
        ]],
        toolbar: '#toolbar-categories',
        // skin: 'line', //表格风格 line （行边框风格）row （列边框风格）nob （无边框风格）
        even: true,   //隔行换色
        page: true, //开启分页
        limits: [10, 20, 50],  //每页条数的选择项，默认：[10,20,30,40,50,60,70,80,90]。
        limit: 10, //每页默认显示的数量
        parseData: function (res) {
            //res 即为原始返回的数据
            return {
                code: res.code, //解析接口状态
                msg: res.message, //解析提示文本
                count: res.count, //解析数据长度
                data: res.data, //解析数据列表
            };
        },
        // 设置响应数据字段名称
        response: {
            statusCode: 20000000, //规定成功的状态码，默认：0
            msgName: "message", //规定状态信息的字段名称，默认：msg
            dataName: "data", //规定数据列表的字段名称，默认：data
        },
    });

    //监听行工具事件
    table.on('tool(filter-category-table)', function (obj) {
        var data = obj.data;
        if (obj.event === 'del') {
            layer.confirm('确定删除？', function (index) {
                $.ajax({
                    url: '/category/' + data.id,
                    method: 'Delete',
                    dataType: 'JSON',
                    success: function (result) {
                        console.log(result)
                        if (result.code === 20003002) {
                            obj.del();
                            layer.close(index);
                            layer.msg(result.msg, {icon: 6});
                        } else {
                            layer.msg(result.msg, {icon: 5});
                        }
                    }
                })
            });
        } else if (obj.event === 'edit') {
            layer.open({
                type: 2,
                title: ['更新分类', 'font-size:1.125rem;'],
                skin: 'layui-layer-molv',
                area: ['50%', '50%'],
                icon: 1,
                content: '/admin/category/' + data.id,
                closeBtn: 1,
                shade: 0.2,
                resize: false,
            }, function (value, index) {
                obj.update({
                    email: value
                });
                layer.close(index);
            });
        }
    });

    table.on('toolbar(filter-category-table)', function (obj) {
        switch (obj.event) {
            case 'add':
                layer.open({
                    type: 2,
                    title: ['创建分类', 'font-size:1.125rem;'],
                    skin: 'layui-layer-molv',
                    area: ['50%', '50%'],
                    icon: 1,
                    content: '/admin/category',
                    // btn: ['提交', '取消'],
                    // yes: function (index, layero) {
                    //     form.on('submit(addCatecory)', function (data) {
                    //         console.log("data.elem" + data.elem)
                    //         console.log("data.field" + data.field)
                    //         var form_data = {form_data: JSON.stringify(form.val('add_category_form'))} //获取表单那数据
                    //         console.log('form_data:' + form_data);
                    //         $.ajax({
                    //             url: '/admin/category',
                    //             method: 'post',
                    //             data: form_data,
                    //             dataType: 'JSON',
                    //             success: function (result) {
                    //                 if (result.code === 0) {
                    //                     layer.close(index);
                    //                     layer.msg(result.msg, {icon: 6});
                    //                 } else {
                    //                     layer.msg(result.msg, {icon: 5});
                    //                 }
                    //             }
                    //         })
                    //         return false;
                    //     })
                    // },
                    // btn2: function (index, layero) {
                    //     layer.close(index); // 关闭弹出层
                    // },
                    // success: function (index, layero) {
                    //     $(layero).find('.layui-layer-btn0').attr({
                    //         'lay-filter': 'addCatecory',
                    //         'lay-submit': 'submit'
                    //     });
                    //
                    // },
                    // btnAlign: 'c',
                    closeBtn: 1,
                    shade: 0.2,
                    resize: false,

                })
                break;
        }
    });


    form.on('submit(filter-button-add-category)', function (data) {
        var form_data = form.val('filter-form-add-category');
        console.log("form");
        console.log(data);
        $.ajax({
            type: 'post',
            url: '/admin/category',
            dataType: 'json',
            data: JSON.stringify(form_data),
            success: function (data) {
                console.log(data)
                table.render()
            }
        })
        return false;
    })


})
;

