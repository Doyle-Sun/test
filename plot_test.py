图 = 1





    sim1 = Simulation_Benchmark(d); gdd, global_machine_times = sim1.gdd, sim1.global_machine_times
    def 图1画图代码():
        plt.rcParams['legend.fontsize'] = 10
        plt.rcParams["font.family"] = "Times New Roman"
        plt.rcParams['mathtext.fontset'] = 'stix'
        plt.rcParams['font.size'] = 14.0
        plt.rcParams['legend.fontsize'] = 12.5
        plt.style.use('classic')
        font = {'family':'Times New Roman', 'weight':'normal', 'size':14}

        fig, axes = plt.subplots(nrows=6, ncols=1, dpi=150, facecolor='w', figsize=(8,6), sharex=True)

        ax = axes[0]
        ax.plot(global_machine_times, gdd['CTRL.cmd_rpm'])
        ax.plot(global_machine_times, gdd['CTRL.omega_r_mech'])
        ax.set_ylabel(r'Speed [r/min]', multialignment='center', fontdict=font)

        ax = axes[1]
        ax.plot(global_machine_times, gdd['CTRL.cmd_idq[0]'])
        ax.plot(global_machine_times, gdd['CTRL.idq[0]'])
        # ax.plot(global_machine_times, gdd['ACM.iD'])
        ax.set_ylabel(r'$i_d$ [A]', multialignment='center', fontdict=font)

        ax = axes[2]
        ax.plot(global_machine_times, gdd['CTRL.cmd_idq[1]'])
        ax.plot(global_machine_times, gdd['CTRL.idq[1]'])
        ax.set_ylabel(r'$i_q$ [A]', multialignment='center', fontdict=font)

        ax = axes[3]
        ax.plot(global_machine_times, gdd['ACM.Tem'])
        ax.plot(global_machine_times, gdd['CTRL.Tem'])
        ax.set_ylabel(r'Tem [Nm]', multialignment='center', fontdict=font)

        ax = axes[4]
        ax.plot(global_machine_times, (gdd['ACM.udq[0]'])) # lpf1_inverter
        ax.plot(global_machine_times, gdd['CTRL.cmd_udq[0]'])
        ax.set_ylabel(r'd-axis votages [V]', multialignment='center', fontdict=font)

        ax = axes[5]
        ax.plot(global_machine_times, (gdd['ACM.udq[1]'])) # lpf1_inverter
        ax.plot(global_machine_times, gdd['CTRL.cmd_udq[1]'])
        ax.set_ylabel(r'q-axis votages [V]', multialignment='center', fontdict=font)

        # ax = axes[6]
        # ax.plot(global_machine_times, gdd['CTRL.uab[0]'])
        # ax.plot(global_machine_times, gdd['CTRL.uab[1]'])
        # ax.set_ylabel(r'raw dq votages [V]', multialignment='center', fontdict=font)

        for ax in axes:
            ax.grid(True)
            for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
                tick.label.set_font(font)
        axes[-1].set_xlabel('Time [s]', fontdict=font)
        return fig
    fig = 图1画图代码(); fig.savefig(f'Shizhou-fig-{图}.pdf', dpi=400, bbox_inches='tight', pad_inches=0)
