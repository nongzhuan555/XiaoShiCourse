<template>
	<view class="date-bar-wrap">
		<view class="left-month">10月</view>
		<view class="right-week-day">
			<view class="right-item">
				<view class="right-item-top">一</view>
				<view class="right-item-btm">28</view>
			</view>
			<view class="right-item">
				<view class="right-item-top">二</view>
				<view class="right-item-btm">29</view>
			</view>
			<view class="right-item">
				<view class="right-item-top">三</view>
				<view class="right-item-btm">30</view>
			</view>
			<view class="right-item">
				<view class="right-item-top">四</view>
				<view class="right-item-btm">31</view>
			</view>
			<view class="right-item">
				<view class="right-item-top">五</view>
				<view class="right-item-btm">1</view>
			</view>
			<view class="right-item">
				<view class="right-item-top">六</view>
				<view class="right-item-btm">2</view>
			</view>
			<view class="right-item">
				<view class="right-item-top">日</view>
				<view class="right-item-btm">3</view>
			</view>
		</view>
	</view>
</template>

<script setup>
	
</script>

<style lang="scss" scoped>
	.date-bar-wrap{
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: space-around;
		align-items: center;
		.left-month{
			width: 10%;
			height: 100%;
			background-color: royalblue;
		}
		.right-week-day{
			width: 90%;
			height: 100%;
			display: flex;
			justify-content: space-around;
			align-items: center;
			.right-item{
				width: 14.25%;
				height: 100%;
				display: flex;
				flex-direction: column;
				justify-content: space-around;
				align-items: center;
				.right-item-top{
					display: flex;
					justify-content: center;
					align-items: center;
					width: 100%;
					height: 100%;
					font-weight: bold;
				}
				.right-item-btm{
					display: flex;
					justify-content: center;
					align-items: center;
					width: 100%;
					height: 100%;
					color:#457B9D;
					font-size: 3vw;
					font-weight: bold;
				}
			}
		}
	}
</style>