<template>
	<view class="left-aside-wrap">
		<view class="left-aside-item">
			<view>
				<p class="top">1</p>
				<p class="btm">08:10</p>
				<p class="btm">08:55</p>
			</view>
			<view>
				<p class="top">2</p>
				<p class="btm">09:05</p>
				<p class="btm">09:50</p>
			</view>
		</view>
		<view class="left-aside-item">
			<view>
				<p class="top">3</p>
				<p class="btm">10:10</p>
				<p class="btm">10:55</p>
			</view>
			<view>
				<p class="top">4</p>
				<p class="btm">11:05</p>
				<p class="btm">11:50</p>
			</view>
		</view>
		<view class="left-aside-item">
			<view>
				<p class="top">5</p>
				<p class="btm">14:20</p>
				<p class="btm">15:05</p>
			</view>
			<view>
				<p class="top">6</p>
				<p class="btm">15:15</p>
				<p class="btm">16:00</p>
			</view>
		</view>
		<view class="left-aside-item">
			<view>
				<p class="top">7</p>
				<p class="btm">16:20</p>
				<p class="btm">17:05</p>
			</view>
			<view>
				<p class="top">8</p>
				<p class="btm">17:15</p>
				<p class="btm">18:00</p>
			</view>
		</view>
		<view class="left-aside-item">
			<view>
				<p class="top">9</p>
				<p class="btm">19:30</p>
				<p class="btm">20:15</p>
			</view>
			<view>
				<p class="top">10</p>
				<p class="btm">20:25</p>
				<p class="btm">21:10</p>
			</view>
		</view>
	</view>
</template>

<style lang="scss" scoped>
	.left-aside-wrap{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-around;
		.left-aside-item{
			width: 100%;
			height: 19.8%;
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: space-around;
			// border-bottom: 1px solid black;
			view{
				display: flex;
				flex-direction: column;
				align-items: center;
				justify-content: center;
				.top{
					font-size: 1.3vw;
					font-weight: bolder;
				}
				.btm{
					font-size: .8vw;
					color:#457B9D
				}
			}
		}
	}
</style>