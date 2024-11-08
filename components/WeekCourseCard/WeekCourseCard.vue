<template>
		<!-- 一个组件是一周 -->
		<view class="week-course-card-wrap">
			<!-- 一周七天 -->
			<view class="week-course-card-week-order" v-for="week_order in 7">
				<!-- 一天五大节课 -->
				<view class="week-course-card-course-order" v-for="course_order in 5">
					<view class="isCourse" v-if="
					course_this_week[week_order.toString()+'-'+course_order.toString()]
					">
						<AtomicCard 
						:course_this_card="course_this_week[week_order.toString()+'-'+course_order.toString()]">
						</AtomicCard>
					</view>
					<view class="noCourse" v-else>
						&nbsp;
					</view>
				</view>
			</view>
		</view>
</template>

<script setup>
	// 通过父组件传值确定该组件该渲染第几周课程
	const props = defineProps(['prop_week_num'])
	let week_key = props.prop_week_num
	const data = uni.getStorageSync('xiaoshi')
	let total_course = data.total_term_courses
	// 获取该周全部课程
	const course_this_week = total_course[week_key.toString()]
	
</script>

<style lang="scss" scoped>
	.week-course-card-wrap{
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: space-around;
		align-items: center;
		.week-course-card-week-order{
			width: 14.25%;
			height: 100%;
			display: flex;
			flex-direction: column;
			justify-content: space-around;
			align-items: center;
			.week-course-card-course-order{
				width: 100%;
				height: 20%;
				display: flex;
				justify-content: center;
				align-items: center;
				border-radius: 1%;
				// border-right: .2px solid red;
				// border-left: .2px solid red;
				// border-bottom: .1px solid red;
				// border-top: .1px solid red;
				.isCourse{
					width: 98%;
					height: 99%;
				}
			}
		}
	}
</style>