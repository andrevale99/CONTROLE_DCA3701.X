/*
 * coupled_tanks_data.c
 *
 * Code generation for model "coupled_tanks".
 *
 * Model version              : 1.300
 * Simulink Coder version : 8.9 (R2015b) 13-Aug-2015
 * C source code generated on : Wed Dec 11 09:18:40 2024
 *
 * Target selection: quarc_win64.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "coupled_tanks.h"
#include "coupled_tanks_private.h"

/* Block parameters (auto storage) */
P_coupled_tanks_T coupled_tanks_P = {
  10.0,                                /* Mask Parameter: HILInitialize_analog_input_maxi
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  -10.0,                               /* Mask Parameter: HILInitialize_analog_input_mini
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  10.0,                                /* Mask Parameter: HILInitialize_analog_output_max
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  -10.0,                               /* Mask Parameter: HILInitialize_analog_output_min
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1.5,                                 /* Mask Parameter: CompareToConstant2_const
                                        * Referenced by: '<S5>/Constant'
                                        */
  29.0,                                /* Mask Parameter: CompareToConstant3_const
                                        * Referenced by: '<S6>/Constant'
                                        */
  27.0,                                /* Mask Parameter: CompareToConstant_const
                                        * Referenced by: '<S3>/Constant'
                                        */
  28.0,                                /* Mask Parameter: CompareToConstant1_const
                                        * Referenced by: '<S4>/Constant'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_final_analog_outp
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_final_pwm_outputs
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_initial_analog_ou
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_initial_pwm_outpu
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  24305.934065934067,                  /* Mask Parameter: HILInitialize_pwm_frequency
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_pwm_leading_deadb
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_pwm_trailing_dead
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_set_other_outputs
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_set_other_outpu_d
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_set_other_outpu_p
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_set_other_outpu_f
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_watchdog_analog_o
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0.0,                                 /* Mask Parameter: HILInitialize_watchdog_pwm_outp
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */

  /*  Mask Parameter: HILInitialize_hardware_clocks
   * Referenced by: '<S2>/HIL Initialize'
   */
  { 0, 1, 2 },
  0,                                   /* Mask Parameter: HILInitialize_initial_encoder_c
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_pwm_alignment
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_pwm_configuration
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_pwm_modes
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_pwm_polarity
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_watchdog_digital_
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */

  /*  Mask Parameter: HILInitialize_analog_input_chan
   * Referenced by: '<S2>/HIL Initialize'
   */
  { 0U, 1U, 2U, 3U, 4U, 5U, 6U, 7U },

  /*  Mask Parameter: HILInitialize_analog_output_cha
   * Referenced by: '<S2>/HIL Initialize'
   */
  { 0U, 1U, 2U, 3U, 4U, 5U, 6U, 7U },

  /*  Mask Parameter: HILReadAnalog_channels
   * Referenced by: '<S2>/HIL Read Analog'
   */
  { 0U, 1U },
  0U,                                  /* Mask Parameter: HILWriteAnalog_channels
                                        * Referenced by: '<S2>/HIL Write Analog'
                                        */

  /*  Mask Parameter: HILInitialize_encoder_channels
   * Referenced by: '<S2>/HIL Initialize'
   */
  { 0U, 1U, 2U, 3U, 4U, 5U, 6U, 7U },

  /*  Mask Parameter: HILInitialize_pwm_channels
   * Referenced by: '<S2>/HIL Initialize'
   */
  { 0U, 1U, 2U, 3U, 4U, 5U, 6U, 7U },
  4U,                                  /* Mask Parameter: HILInitialize_quadrature
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_active
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_final_digital_out
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_initial_digital_o
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_analog_input_
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_analog_inpu_h
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_analog_output
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_analog_outp_c
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_analog_outp_o
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_analog_outp_e
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_analog_outp_b
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_analog_outp_h
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_analog_out_bm
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_clock_frequen
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_clock_frequ_i
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_clock_params_
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_clock_param_n
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_digital_outpu
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_digital_out_l
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_digital_out_k
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_digital_out_o
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_digital_out_j
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_digital_ou_ol
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_digital_out_i
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_encoder_count
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_encoder_cou_e
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_encoder_param
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_encoder_par_a
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_other_outpu_a
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_pwm_outputs_a
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_pwm_outputs_i
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_pwm_outputs_j
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_pwm_outputs_b
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_pwm_outputs_o
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  1,                                   /* Mask Parameter: HILInitialize_set_pwm_params_at
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  0,                                   /* Mask Parameter: HILInitialize_set_pwm_params__e
                                        * Referenced by: '<S2>/HIL Initialize'
                                        */
  4.0,                                 /* Expression: 4
                                        * Referenced by: '<S1>/Saturation'
                                        */
  -4.0,                                /* Expression: -4
                                        * Referenced by: '<S1>/Saturation'
                                        */
  6.25,                                /* Expression: 30/4.8
                                        * Referenced by: '<S2>/Volts to cm Tank 1 '
                                        */
  6.25,                                /* Expression: 30/4.8
                                        * Referenced by: '<S2>/Volts to cm Tank 2'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S7>/Constant'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<Root>/Integrator_e'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<Root>/Integrator_m'
                                        */
  5.0,                                 /* Expression: 5
                                        * Referenced by: '<Root>/Constant'
                                        */
  1.2,                                 /* Expression: 1.2
                                        * Referenced by: '<Root>/Kp_m'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<Root>/Integrator_gain'
                                        */
  0.1,                                 /* Expression: 0.1
                                        * Referenced by: '<Root>/N_m (filter gain)'
                                        */
  0.4,                                 /* Expression: 0.4
                                        * Referenced by: '<Root>/kd_m '
                                        */
  1.0,                                 /* Expression: 1
                                        * Referenced by: '<Root>/Kp_e'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<Root>/Integrator_gain2'
                                        */
  0.8,                                 /* Expression: 0.8
                                        * Referenced by: '<Root>/N_m (filter gain)1'
                                        */
  0.8,                                 /* Expression: 0.8
                                        * Referenced by: '<Root>/kd_e'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S8>/Constant'
                                        */
  3.0,                                 /* Expression: 3
                                        * Referenced by: '<S1>/Op Normal'
                                        */
  1.5,                                 /* Expression: 1.5
                                        * Referenced by: '<S1>/Mantem A bomba em 30cm'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S1>/Desliga a bomba'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<Root>/Kaw = Kp // taw'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<Root>/Ki_e'
                                        */
  0.2,                                 /* Expression: 0.2
                                        * Referenced by: '<Root>/Ki_m  '
                                        */
  32768U,                              /* Computed Parameter: Gain_Gain
                                        * Referenced by: '<S1>/Gain'
                                        */
  1,                                   /* Computed Parameter: HILReadAnalog_Active
                                        * Referenced by: '<S2>/HIL Read Analog'
                                        */
  0                                    /* Computed Parameter: HILWriteAnalog_Active
                                        * Referenced by: '<S2>/HIL Write Analog'
                                        */
};
