<template>
	<view class="index-wrap">
		<view class="index-topbar">
			<!-- 已实现 -->
			<view class="topbar-week-state">
				<text>第
				<text>{{current_week_index}}</text>
				&nbsp;周</text>
			</view>
		</view>
		<view class="index-coursetable">
			<CourseTable @changeParentData='acceptChildData'></CourseTable>
		</view>
	</view>
</template>

<script setup>
	import { ref } from 'vue'
	const current_week_index = ref(1)
	const acceptChildData = (current_week) => {
		current_week_index.value = current_week
	}
</script>

<style lang="scss" scoped>
	.topbar-week-state{
		background-color: #fff;
		display: flex;
		flex-direction: column;
		justify-content: center;
		width: 100%;
		height: 100%;
		text{
			color: #ff7e00;
			font-weight: bolder;
			margin-left: 5vw;
			text{
				color: black;
			}
		}
	}
	.index-wrap{
		width: 100%;
		height: 100vh;
		display: flex;
		flex-direction: column;
		justify-content: start;
		align-items: center;
		background-color: #fff;
		.index-topbar{
			width: 100%;
			height: 3vh;
		}
		.index-coursetable{
			width: 100%;
			height: 97vh;
		}
	}
</style>