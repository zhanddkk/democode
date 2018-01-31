/***********************************************************************************************************************
 * Original Author : Register Map File Generation Tool (v0.0.1)
 * File Path       : regmap.h
 * Item Number     : 4
 *
 * Please don't edit this file manually!!!
***********************************************************************************************************************/
#ifndef _REGMAP_H_
#define _REGMAP_H_
#include <stdint.h>

#define __I     volatile const       /*!< Defines 'read only' permissions */
#define __O     volatile             /*!< Defines 'write only' permissions */
#define __IO    volatile             /*!< Defines 'read / write' permissions */

/*====================================================================================================================*/
/* System Control: 43 members */
/*--------------------------------------------------------------------------------------------------------------------*/
struct system_control_reg_map {
    __IO uint32_t APLL_LOCK; /* 0x7E00F000: Control PLL locking period for APLL 0x0000_FFFF */
    __IO uint32_t MPLL_LOCK; /* 0x7E00F004: Control PLL locking period for MPLL 0x0000_FFFF */
    __IO uint32_t EPLL_LOCK; /* 0x7E00F008: Control PLL locking period for EPLL 0x0000_FFFF */
    __IO uint32_t APLL_CON; /* 0x7E00F00C: Control PLL output frequency for APLL 0x0190_0302 */
    __IO uint32_t MPLL_CON; /* 0x7E00F010: Control PLL output frequency for MPLL 0x0214_0603 */
    __IO uint32_t EPLL_CON0; /* 0x7E00F014: Control PLL output frequency for EPLL 0x0020_0102 */
    __IO uint32_t EPLL_CON1; /* 0x7E00F018: Control PLL output frequency for EPLL 0x0000_9111 */
    __IO uint32_t CLK_SRC; /* 0x7E00F01C: Select clock source 0x0000_0000 */
    __IO uint32_t CLK_DIV0; /* 0x7E00F020: Set clock divider ratio 0x0105_1000 */
    __IO uint32_t CLK_DIV1; /* 0x7E00F024: Set clock divider ratio 0x0000_0000 */
    __IO uint32_t CLK_DIV2; /* 0x7E00F028: Set clock divider ratio 0x0000_0000 */
    __IO uint32_t CLK_OUT; /* 0x7E00F02C: Select clock output 0x0000_0000 */
    __IO uint32_t HCLK_GATE; /* 0x7E00F030: Control HCLK clock gating 0xFFFF_FFFF */
    __IO uint32_t PCLK_GATE; /* 0x7E00F034: Control PCLK clock gating 0xFFFF_FFFF */
    __IO uint32_t SCLK_GATE; /* 0x7E00F038: Control SCLK clock gating 0xFFFF_FFFF */
    __IO uint32_t MEM0_CLK_GATE; /* 0x7E00F03C: Control MEM0 clock gating 0xFFFF_FFFF */
    __O uint32_t RESERVED_0[48]; /* 0x7E00F040 ~ 0x7E00F0FC: RESERVED - */
    __IO uint32_t AHB_CON0; /* 0x7E00F100: Configure AHB I/P/X/F bus 0x0400_0000 */
    __IO uint32_t AHB_CON1; /* 0x7E00F104: Configure AHB M1/M0/T1/T0 bus 0x0000_0000 */
    __IO uint32_t AHB_CON2; /* 0x7E00F108: Configure AHB R/S1/S0 bus 0x0000_0000 */
    __IO uint32_t CLK_SRC2; /* 0x7E00F10C: Select Audio2 clock source 0x0000_0000 */
    __IO uint32_t SDMA_SEL; /* 0x7E00F110: Select secure DMA input 0x0000_0000 */
    __IO uint32_t RESERVED_1; /* 0x7E00F114: RESERVED 0x0000_0000 */
    __O uint32_t SYS_ID; /* 0x7E00F118: System ID for revision and pass 0x3641_0101 */
    __IO uint32_t SYS_OTHERS; /* 0x7E00F11C: SYSCON others control register 0x0000_0000 */
    __IO uint32_t MEM_SYS_CFG; /* 0x7E00F120: Configure memory subsystem 0x0000_0080 */
    __IO uint32_t RESERVED_2; /* 0x7E00F124: RESERVED 0x0000_0000 */
    __IO uint32_t QOS_OVERRIDE1; /* 0x7E00F128: Override DMC1 QOS 0x0000_0000 */
    __O uint32_t MEM_CFG_STAT; /* 0x7E00F12C: Memory subsystem setup status 0x0000_0000 */
    __IO uint32_t RESERVED_3; /* 0x7E00F130: Should be 0x0 0x0000_0000 */
    __O uint32_t RESERVED_4[51]; /* 0x7E00F134 ~ 0x7E00F1FC: RESERVED - */
    __IO uint32_t RESERVED_5[16]; /* 0x7E00F200 ~ 0x7E00F23C: Should be 0x0 0x0000_0000~0x0000_0000 */
    __O uint32_t RESERVED_6[369]; /* 0x7E00F240 ~ 0x7E00F800: RESERVED - */
    __IO uint32_t PWR_CFG; /* 0x7E00F804: Configure power manager 0x0000_0001 */
    __IO uint32_t EINT_MASK; /* 0x7E00F808: Configure EINT(external interrupt) mask 0x0000_0000 */
    __O uint32_t RESERVED_7; /* 0x7E00F80C: RESERVED - */
    __IO uint32_t NORMAL_CFG; /* 0x7E00F810: Configure power manager at NORMAL mode 0xFFFF_FF00 */
    __IO uint32_t STOP_CFG; /* 0x7E00F814: Configure power manager at STOP mode 0x2012_0100 */
    __IO uint32_t SLEEP_CFG; /* 0x7E00F818: Configure power manager at SLEEP mode 0x0000_0000 */
    __IO uint32_t STOP_MEM_CFG; /* 0x7E00F81C: Configure memory power at STOP mode 0x0000_007f */
    __IO uint32_t OSC_FREQ; /* 0x7E00F820: Oscillator frequency scale counter 0x0000_000F */
    __IO uint32_t OSC_STABLE; /* 0x7E00F824: Oscillator pad stable counter 0x0000_0001 */
    __IO uint32_t PWR_STABLE; /* 0x7E00F828: Power stable counter 0x0000_0001 */
    __O uint32_t RESERVED_8; /* 0x7E00F82C: RESERVED - */
    __IO uint32_t MTC_STABLE; /* 0x7E00F830: MTC stable counter 0xFFFF_FFFF */
    __IO uint32_t BUS_CACHEABLE_CON; /* 0x7E00F834: Decision whether packing is used or not - */
    __IO uint32_t MISC_CON; /* 0x7E00F838: Bus control 0x0000_0000 */
    __O uint32_t RESERVED_9[49]; /* 0x7E00F83C ~ 0x7E00F8FC: RESERVED - */
    __IO uint32_t OTHERS; /* 0x7E00F900: Others control register 0x0000_801E */
    __O uint32_t RST_STAT; /* 0x7E00F904: Reset status register 0x0000_0001 */
    __IO uint32_t WAKEUP_STAT; /* 0x7E00F908: Wakeup status register 0x0000_0000 */
    __O uint32_t BLK_PWR_STAT; /* 0x7E00F90C: Block power status register 0x0000_00FF */
} volatile *const r_system_control = (void *)0x7E00F000;
/*====================================================================================================================*/
/* User Information: 4 members */
/*--------------------------------------------------------------------------------------------------------------------*/
struct user_information_reg_map {
    __IO uint32_t INFORM0; /* 0x7E00FA00: Information register0 0x0000_0000 */
    __IO uint32_t INFORM1; /* 0x7E00FA04: Information register1 0x0000_0000 */
    __IO uint32_t INFORM2; /* 0x7E00FA08: Information register2 0x0000_0000 */
    __IO uint32_t INFORM3; /* 0x7E00FA0C: Information register3 0x0000_0000 */
} volatile *const r_user_information = (void *)0x7E00FA00;
/*====================================================================================================================*/
/* UART 0: 15 members */
/*--------------------------------------------------------------------------------------------------------------------*/
struct uart_0_reg_map {
    __IO uint32_t ULCON0; /* 0x7F005000: UART channel 0 line control register 0x00 */
    __IO uint32_t UCON0; /* 0x7F005004: UART channel 0 control register 0x00 */
    __IO uint32_t UFCON0; /* 0x7F005008: UART channel 0 FIFO control register 0x0 */
    __IO uint32_t UMCON0; /* 0x7F00500C: UART channel 0 Modem control register 0x0 */
    __O uint32_t UTRSTAT0; /* 0x7F005010: UART channel 0 Tx/Rx status register 0x6 */
    __O uint32_t UERSTAT0; /* 0x7F005014: UART channel 0 Rx error status register 0x0 */
    __O uint32_t UFSTAT0; /* 0x7F005018: UART channel 0 FIFO status register 0x00 */
    __O uint32_t UMSTAT0; /* 0x7F00501C: UART channel 0 Modem status register 0x0 */
    __I uint32_t UTXH0; /* 0x7F005020: UART channel 0 transmit buffer register - */
    __O uint32_t URXH0; /* 0x7F005024: UART channel 0 receive buffer register 0x00 */
    __IO uint32_t UBRDIV0; /* 0x7F005028: UART channel 0 Baud rate divisior register 0x0000 */
    __IO uint32_t UDIVSLOT0; /* 0x7F00502C: UART channel 0 Dividing slot register 0x0000 */
    __IO uint32_t UINTP0; /* 0x7F005030: UART channel 0 Interrupt Pending Register 0x0 */
    __IO uint32_t UINTSP0; /* 0x7F005034: UART channel 0 Interrupt Source Pending Register 0x0 */
    __IO uint32_t UINTM0; /* 0x7F005038: UART channel 0 Interrupt Mask Register 0x0 */
} volatile *const r_uart_0 = (void *)0x7F005000;
/*====================================================================================================================*/
/* UART 1: 15 members */
/*--------------------------------------------------------------------------------------------------------------------*/
struct uart_1_reg_map {
    __IO uint32_t ULCON1; /* 0x7F005400: UART channel 1 line control register 0x00 */
    __IO uint32_t UCON1; /* 0x7F005404: UART channel 1 control register 0x00 */
    __IO uint32_t UFCON1; /* 0x7F005408: UART channel 1 FIFO control register 0x0 */
    __IO uint32_t UMCON1; /* 0x7F00540C: UART channel 1 Modem control register 0x0 */
    __O uint32_t UTRSTAT1; /* 0x7F005410: UART channel 1 Tx/Rx status register 0x6 */
    __O uint32_t UERSTAT1; /* 0x7F005414: UART channel 1 Rx error status register 0x0 */
    __O uint32_t UFSTAT1; /* 0x7F005418: UART channel 1 FIFO status register 0x00 */
    __O uint32_t UMSTAT1; /* 0x7F00541C: UART channel 1 Modem status register 0x0 */
    __I uint32_t UTXH1; /* 0x7F005420: UART channel 1 transmit buffer register - */
    __O uint32_t URXH1; /* 0x7F005424: UART channel 1 receive buffer register 0x00 */
    __IO uint32_t UBRDIV1; /* 0x7F005428: UART channel 1 Baud rate divisior register 0x0000 */
    __IO uint32_t UDIVSLOT1; /* 0x7F00542C: UART channel 1 Dividing slot register 0x0000 */
    __IO uint32_t UINTP1; /* 0x7F005430: UART channel 1 Interrupt Pending Register 0x0 */
    __IO uint32_t UINTSP1; /* 0x7F005434: UART channel 1 Interrupt Source Pending Register 0x0 */
    __IO uint32_t UINTM1; /* 0x7F005438: UART channel 1 Interrupt Mask Register 0x0 */
} volatile *const r_uart_1 = (void *)0x7F005400;
#endif /* _REGMAP_H_ */