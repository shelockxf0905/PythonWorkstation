"""
    作者：xiao-yi.yu
    功能：五角星的绘制
    版本：2.0
    日期：2019/09/22
    新增功能：加入循环操作绘制重复不同大小的图形
"""
import turtle

def draw_pentagram(size):
    """
        绘制五角星
    """
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1


def draw_recursive_pentagram(size):
    """
        迭代绘制五角星
    """
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1

    # 五角星绘制完成，更新参数
    size += 100
    if size <= 600:
        draw_recursive_pentagram(size)

def main():
    """
        主函数
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 100
    draw_recursive_pentagram(size)

    turtle.exitonclick()

if __name__ == '__main__':
    main()
