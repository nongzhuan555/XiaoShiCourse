<template>
	<view class="atomic-card-wrap">
		<view class="course-name">
			{{ course.course_name }}
		</view>
		<view class="course-site">
			{{ course.classroom }}
		</view>
	</view>
</template>

<script setup>
	const prop = defineProps(['course_this_card'])
	const course = prop.course_this_card
	const color_value = course.teacher
	console.log(color_value)
	console.log(typeof(color_value))
</script>

<style lang="scss" scoped>
	.atomic-card-wrap{
		// width: 13vw;
		// height: 18vh;
		width: 98%;
		height: 99%;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		align-items: center;
		// border: 1px solid black;
		border-radius: 1vh;
		background-color: lightcyan;
		.course-name{
			display: flex;
			justify-content: center;
			align-items: center;
			width: 95%;
			height: 70%;
			font-size: 1.7vw;
		}
		.course-site{
			display: flex;
			justify-content: center;
			align-items: center;
			width: 95%;
			height: 30%;
			font-size: 1.2vw;
			font-weight: bold;
		}
	}
</style>