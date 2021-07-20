<script>
    var myChart = echarts.init(document.getElementById('main'));

    var categories = [];
    categories[0] = {
        name: '主要人物'
    };
    categories[1] = {
        name: '其它人物'
    };
    
    option = {
        // 图的标题
        title: {
            x:'middle',
            text: '觉醒年代人物关系图'
        },
        //图的位置
        // grid: {
        //       bottom: 150,
        //       top: 0,
        //       right: 0,
        //       left: 0,
        //       height: 300
        //     },
        // 提示框的配置
        tooltip: {
            formatter: function (x) {
                return x.data.des;
            }
        },
        // 工具箱
        toolbox: {
            // 显示工具箱
            show: true,
            feature: {
                mark: { 
                    show: true
                   
                },
                // 还原
                restore: {
                    show: true
                },
                // 保存为图片
                saveAsImage: {
                    show: true
                }
            }
        },
        legend: [{
            // selectedMode: 'single',
            x:'left',
            data: categories.map(function (a) {
                return a.name;
            })
        }],
        series: [{
            type: 'graph', // 类型:关系图
            layout: 'force', //图的布局，类型为力导图
            symbolSize: 50, // 调整节点的大小
            roam: false, // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移,可以设置成 'scale' 或者 'move'。设置成 true 为都开启
            edgeSymbol: ['circle', 'arrow'],
            edgeSymbolSize: [2, 10],
            edgeLabel: {
                normal: {
                    textStyle: {
                        fontSize: 20
                    }
                }
            },
            force: {
                repulsion: 2500,
                edgeLength: [10, 50]
            },
            draggable: true,
            lineStyle: {
                normal: {
                    width: 2,
                    color: '#4b565b',
                }
            },
            edgeLabel: {
                normal: {
                    show: true,
                    formatter: function (x) {
                        return x.data.name;
                    }
                }
            },
            label: {
                normal: {
                    show: true,
                    textStyle: {}
                }
            },
            
 
            // 数据
            data: [{
                name: '陈独秀',
                des: '倡导新文化运动',
                symbolSize: 60,
                category: 0,
            }, {
                name: '李大钊',
                des: '北京大学图书馆主任，革命先驱',
                symbolSize: 60,
                category: 0,
            }, {
                name: '陈延年',
                des: '震旦学校学生，革命烈士',
                symbolSize: 60,
                category: 1,
            }, {
                name: '辜鸿铭',
                des: '北京大学教授',
                symbolSize: 60,
                category: 0,
            }, {
                name: '周恩来',
                des: '南开学校学生，中共早期党员',
                symbolSize: 60,
                category: 1,
            },{
                name: '毛泽东',
                des: '北京大学图书管理员，中国共产党创始人之一',
                symbolSize: 60,
                category: 0,
            },{
                name: '胡适',
                des: '北京大学教授',
                symbolSize: 60,
                category: 0,
            },{
                name: '蔡元培',
                des: '北大校长',
                symbolSize: 60,
                category:0,
            },{
                name: '赵世炎',
                des: '师大附中学生会干事长',
                symbolSize: 60,
                category: 1,
            },{
                name: '邓中夏',
                des: '北京大学学生',
                symbolSize: 60,
                category: 1,
            },{
                name: '高君曼',
                des: '陈独秀夫人',
                symbolSize: 60,
                category: 1,
            },{
                name: '鲁迅',
                des: '北京大学兼职教师，号召“白话文运动”',
                symbolSize: 60,
                category: 0,
            },{
                name: '高君宇',
                des: ' ',
                symbolSize: 60,
                category: 1,
            },{
                name: '瞿秋白',
                des: ' ',
                symbolSize: 60,
                category: 1,
            }],
            links: [{
                source: '陈独秀',
                target: '陈延年',
                name: '父子',
                des: ' '
            }, {
                source: '陈独秀',
                target: '高君曼',
                name: '夫妻',
                des: ' '
            }, {
                source: '陈独秀',
                target: '李大钊',
                name: '合作',
                des: '共同参与编辑《新青年》，推动革命'
            }, {
                source: '鲁迅',
                target: '蔡元培',
                name: '朋友',
                des: '多年革命盟友、朋友'
            }, {
                source: '蔡元培',
                target: '陈独秀',
                name: '聘请',
                des: '蔡元培任北大校长期间聘请陈独秀讲学'
            }, {
                source: '蔡元培',
                target: '李大钊',
                name: '聘请',
                des: '蔡元培任北大校长期间聘请李大钊讲学'
            }, {
                source: '蔡元培',
                target: '辜鸿铭',
                name: '聘请',
                des: '蔡元培任北大校长期间聘请辜鸿铭讲学'
            }, {
                source: '赵世炎',
                target: '陈独秀',
                name: '共事',
                des: '与陈独秀等共同领导和指挥上海工人第三次武装起义'
            }, {
                source: '陈独秀',
                target: '周恩来',
                name: '合作',
                des: '合作des'
            }, {
                source: '鲁迅',
                target: '胡适',
                name: '朋友',
                des: '多年革命盟友、朋友'
            }, {
                source: '鲁迅',
                target: '蔡元培',
                name: '朋友',
                des: '多年革命盟友、朋友'
            }, {
                source: '邓中夏',
                target: '瞿秋白',
                name: '同事',
                des: '共同任教上海大学'
            },{
                source: '李大钊',
                target: '毛泽东',
                name: '良师益友',
                des: '李大钊被毛泽东视为“真正的老师”'
            },{
                source: '陈独秀',
                target: '胡适',
                name: '朋友',
                des: '因《新青年》缔结深厚友谊'
            },{
                source: '陈独秀',
                target: '高君宇',
                name: '同事',
                des: ' '
            },{
                source: '李大钊',
                target: '高君宇',
                name: '同事',
                des: ' '
            },{
                source: '周恩来',
                target: '高君宇',
                name: '朋友',
                des: ' '
            },{
                source: '鲁迅',
                target: '瞿秋白',
                name: '合作',
                des: ' '
            },{
                source: '陈独秀',
                target: '瞿秋白',
                name: '同事',
                des: '陈独秀到莫斯科，瞿秋白担任翻译'
            }],
            categories: categories,
        }]
    };
</script>

