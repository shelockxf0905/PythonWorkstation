"""
    作者：xiao-yi.yu
    功能：利用递归函数绘制分形树
    版本：1.0
    日期：2019/09/22
"""
import turtle

STEP_LEN = 13
ANGLE_VAL = 18

def setColor(size):
    # 设置树枝颜色
    if size <= STEP_LEN * 2:
        turtle.color('green')
        print('这是树枝的末端。 ')
    else:
        turtle.color('brown')

def setPenSize(pensize):
    # 设置树枝颜色
    if pensize > 0:
        turtle.pensize(pensize)
        print('树枝粗： ', pensize)

def draw_branch(branch_length, pensize):
    """
        绘制分形树
    """
    if branch_length > STEP_LEN:
        setColor(branch_length)
        setPenSize(pensize)

        # 绘制右侧树枝
        turtle.forward(branch_length)
        print('向前 ', branch_length)
        turtle.right(ANGLE_VAL)
        print('右转 ', ANGLE_VAL)
        draw_branch(branch_length - STEP_LEN, pensize - 1)

        # 绘制左侧树枝
        turtle.left(ANGLE_VAL * 2)
        print('左转 ', ANGLE_VAL * 2)
        draw_branch(branch_length - STEP_LEN, pensize - 1)

        # 返回之前的树枝
        setColor(branch_length)
        turtle.right(ANGLE_VAL)
        print('右转 ', ANGLE_VAL)
        turtle.backward(branch_length)
        print('向后 ', branch_length)

def main():
    """
        主函数
    """
    BRANCH_LEN = 150

    turtle.left(90)
    turtle.penup()
    turtle.backward(490)
    turtle.pendown()
    turtle.color('brown')
    level = BRANCH_LEN//STEP_LEN
    turtle.pensize(level)
    draw_branch(BRANCH_LEN, level)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
