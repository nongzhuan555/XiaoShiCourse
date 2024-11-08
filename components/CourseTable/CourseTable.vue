<template>
	<view class="coursetable">
		<swiper @change="watchChange">
			<swiper-item v-for="week_order in total_week_num">
				<view class="date-bar">
					<DateBar></DateBar>
				</view>
				<view class="course-content-wrap">
					<view class="left-aside">
						<!-- 不变的 -->
						<LeftAside></LeftAside>
					</view>
					<view class="right-aside">
						<WeekCourseCard :prop_week_num= week_order></WeekCourseCard>
					</view>
				</view>
			</swiper-item>
		</swiper>
	</view>
</template>

<script setup>
	import { ref } from 'vue'
	const data = uni.getStorageSync('xiaoshi')
	// 获取该学期有课的周数,固定的
	const total_week_num = data.total_week_num
	const emits = defineEmits(['changeParentData'])
	const toParent = (data) => {
		emits('changeParentData',data)
	}
	const watchChange = (e) => {
		toParent(e.detail.current+1)
	}
</script>

<style lang="scss" scoped>
	.coursetable{
		width: 100%;
		height: 100%;
		swiper{
			width: 100%;
			height: 100%;
			// background-color: #FFDAB9;
			swiper-item{
				// 其实swiper-item默认撑满容器
				width: 100%;
				height: 100%;
				.date-bar{
					width: 100%;
					height: 7%;
					border-bottom: 1px solid black;
				}
				.course-content-wrap{
					width: 100%;
					height: 93%;
					position: relative;
					.left-aside{
						position: absolute;
						display: inline-block;
						width: 10%;
						height: 100%;
					}
					.right-aside{
						// left: 9.8%;
						right: 0;
						position: absolute;
						display: inline-block;
						width: 90%;
						height: 100%;
					}
				}
			}
		}
	}
</style>